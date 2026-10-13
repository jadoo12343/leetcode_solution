class BusBooking:
    def __init__(self, n: int):
        self.bookings = {}
        self.total = 0

    def toggle(self, seat: str) -> None:
        if seat in self.bookings:
            self.total -= self.bookings.pop(seat)
            return
        middle = {"A": "B", "D": "C"}.get(seat[0], "") + seat[1:]
        self.bookings[seat] = 3 if middle in self.bookings else 1
        self.total += self.bookings[seat]

    def getTotalTime(self) -> int:
        return self.total

    def getMinTime(self) -> int:
        return len(self.bookings)


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()