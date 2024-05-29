const users = []; // Array to store registered users

// Function to handle login
function login(event) {
    event.preventDefault(); // Prevent form submission
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    // Check if user exists
    const user = users.find(user => user.username === username && user.password === password);
    if (user) {
        alert('Login successful!');
        // Here you can redirect the user to a new page or perform any other actions after login
    } else {
        alert('Invalid username or password. Please try again.');
    }
}

// Function to handle registration
function register(event) {
    event.preventDefault(); // Prevent form submission
    const username = document.getElementById('newUsername').value;
    const password = document.getElementById('newPassword').value;

    // Check if username already exists
    const existingUser = users.find(user => user.username === username);
    if (existingUser) {
        alert('Username already exists. Please choose a different one.');
    } else {
        // Add new user to the array
        users.push({ username, password });
        alert('Registration successful! You can now login.');
        // You may also clear the registration form here if needed
    }
}

// Add event listeners to the forms
document.getElementById('loginForm').addEventListener('submit', login);
document.getElementById('registerForm').addEventListener('submit', register);