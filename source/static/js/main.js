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
document.getElementById('vacationForm').addEventListener('submit', function(event) {
    const startDate = document.getElementById('vacation_start').value;
    const endDate = document.getElementById('vacation_end').value;

    if (new Date(startDate) > new Date(endDate)) {
        event.preventDefault(); // Prevent form submission
        alert('End date cannot be before start date.');
    }
});
