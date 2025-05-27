from datetime import date

from fastapi import APIRouter, Depends
# from fastapi_versioning import version

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RooomCannotBeBooked
from app.tasks.tasks import send_confirm_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
# @version(1)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
# @version(1)
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user)
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RooomCannotBeBooked

    booking_schema = SBooking.model_validate(booking)
    booking_dict = booking_schema.model_dump()
    send_confirm_email.delay(booking_dict, user.email)
    return booking_dict

    
@router.delete("/{booking_id}")
# @version(1)
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)
