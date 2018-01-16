/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');

// Ticket section

/*** Cancel the user ticket via ajax on modal button ****/
$(function () {

	//load form
	var load_cancel_ticket = function () {
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType: 'json',
			headers: {"X-CSRFToken": getCookie('csrftoken')}, // prevent CSRF attack,
			beforeSend: function () {
				// $('#modal-cancel-user-ticket .modal-content').html("");
			},
			success: function (data) {
				$("#modal-cancel-user-ticket .modal-content").html(data);
			},
			complete: function (xhr, status) {
				// alert('complete: ' + status);
			}
		});
	};

	var cancel_ticket = function () {
		var form = $(this);
		$.ajax({
			url: form.attr("action"),
			data: form.serialize(),
			type: form.attr("method"),
			dataType: 'json',
			beforeSend: function () {

			},
			success: function (data) {
				// if the ticket was succesfully canceled
				if (data.form_is_valid) {

					//we hide the modal
					$("#modal-cancel-user-ticket").modal("hide");

					//and update the tickets information

					$(".ticket-list .container").html(data.html);
				}
				else {
					$("#modal-cancel-user-ticket .modal-content").html(data);
				}
			},
			complete: function (xhr, status) {
				// alert('complete: ' + status);
			}
		});

		return false;
	};

	// binding events
	$('.ticket-list').on("click", ".js-cancel-ticket", load_cancel_ticket);
	$('#modal-cancel-user-ticket').on("submit", ".js-ticket-cancel", cancel_ticket);
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// var csrftoken = getCookie('csrftoken');
