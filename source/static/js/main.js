// Function to confirm deletion
const confirmation = () => {
  const userConfirmed = confirm(
    "You are about to delete this vacation. Are you sure?"
  );
  if (!userConfirmed) {
    event.preventDefault();
  }
};

// Function to remove error message after a delay
const removeError = () => {
  const errorSpan = document.querySelector(".error");
  if (errorSpan) {
    setTimeout(() => {
      errorSpan.remove();
    }, 3000);
  }
};
(() => {
  removeError();
})();

// Function to preview an image before upload
const previewImage = (event) => {
  const reader = new FileReader();
  reader.onload = () => {
    const previewElement = document.getElementById("preview");
    const previewContainer = document.getElementById("image_preview");

    previewElement.src = reader.result;
    previewElement.style.display = "block";
    previewContainer.classList.add("has-image");
  };
  reader.readAsDataURL(event.target.files[0]);
};



// Function to validate dates
function validateDates(event) {
    const startDate = document.getElementById('vacation_start').value;
    const endDate = document.getElementById('vacation_end').value;
    if (startDate && endDate && new Date(startDate) > new Date(endDate)) {
        event.preventDefault();
        alert('End date cannot be before start date.');
        return false; // Stop further validation if dates are invalid
    }
    return true;
}

// Function to validate price
function validatePrice(event) {
    const price = parseInt(document.getElementById('vacation_price').value, 10);
    if (isNaN(price) || price < 1 || price > 10000) {
        event.preventDefault();
        alert('Price must be between 1 and 10,000.');
        return false; // Stop further validation if price is invalid
    }
    return true;
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('vacationForm');
    if (form) {
        form.addEventListener('submit', function(event) {
            // Call validation functions
            if (!validateDates(event) || !validatePrice(event)) {
                return; // Stop submission if any validation fails
            }
        });
    }
});