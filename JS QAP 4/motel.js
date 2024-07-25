const roomPref = ['Single','Double','Executive'];

let customer = [{
    name: "Bob Smith",
    birthDate: "1998-01-23",
    gender: "Male",
    email: "bobsmith@example.com",
    address: {
        street: "111 Main St.",
        city: "St. John's",
        province: "NL",
        postalCode: "A1A1A1"
    },
    phoneNumber: "(709) 555-1234",
    paymentMethod: "Credit Card",
    roomType: roomPref[0],
    checkInDate: "2024-07-29",
    checkOutDate: "2024-07-31",
    getAge: function() {
        let today = new Date();
        const birthDate = new Date(this.birthDate);
        let age = today.getFullYear() - birthDate.getFullYear();
        return age;
    },
    getStayDuration: function() {
        const checkIn = new Date(this.checkInDate);
        const checkOut = new Date(this.checkOutDate);
        const duration = Math.abs(checkOut - checkIn) / (1000 * 60 * 60 * 24);
        return duration;
    }
}];

console.log(`${customer[0].name} is a ${customer[0].getAge()}-year-old ${customer[0].gender}. ${customer[0].name} prefers a ${customer[0].roomType} room. Their stay duration is ${customer[0].getStayDuration()} days. Their email address is ${customer[0].email}. ${customer[0].name} lives at ${customer[0].address.street}, ${customer[0].address.city}. Their phone number is ${customer[0].phoneNumber}. Their payment method is ${customer[0].paymentMethod}.`);