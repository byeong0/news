(function() {
  'use strict';

  var sidebarToggle = document.querySelector('.sidebar-toggle');
  var sidebarCheckbox = document.querySelector('.sidebar-checkbox');

  if (!sidebarToggle || !sidebarCheckbox) return;

  sidebarToggle.addEventListener('click', function(e) {
    e.preventDefault();
    sidebarCheckbox.checked = !sidebarCheckbox.checked;
  });
})();

