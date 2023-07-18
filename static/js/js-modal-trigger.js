document.addEventListener('DOMContentLoaded', () => {
  // let clickedData;

  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add('is-active');
  }

  function closeModal($el) {
    $el.classList.remove('is-active');
    
      // Perform AJAX request to route to /profile
      // const xhr = new XMLHttpRequest();
      // xhr.open('GET', '/profile', true);
      // xhr.onreadystatechange = function() {
      //   if (xhr.readyState === 4 && xhr.status === 200) {
      //     // Handle the response here
      //     console.log(xhr.responseText);
      //   }
      // };
      // xh
    // $.ajax({
    //   type: "GET",
    //   url: "/profile",
    //   data: JSON.stringify(server_data),
    //   contentType: "application/json",
    //   dataType: 'json' 
    // })
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener('click', () => {
      // clickedData = $trigger.dataset.value;
      openModal($target);
    });
  });

  // Add a click event on various child elements to close the parent modal
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
    const $target = $close.closest('.modal');

    $close.addEventListener('click', () => {
      // closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener('keydown', (event) => {
    const e = event || window.event;

    if (e.keyCode === 27) { // Escape key
      // closeAllModals();
    }
  });
});
