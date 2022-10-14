const $ = window.$;
$(document).ready(() => {
  $('div#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(() => {
    $('li').last().remove();
  });
});
