function initJournal(){
	var indicator = $('#ajax-progress-indicator');
	$('.day-box input[type="checkbox"]').click(function(event){
		var box = $(this);
		$.ajax(box.data('url'), {
			'type':'POST',
			'async':true,
			'dataType':'json',
			'data':{
				'pk': box.data('student-id'),
				'date': box.data('date'),
				'present': box.is(':checked') ? '1' : '',
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
			},
			'beforeSend':function(xhr, settings){
				indicator.show();
			},
			'error':function(xhr, status, error){
				alert(error);
				indicator.hide();
			},
			'success': function(data, status, xhr){
				indicator.hide();
			}
		});
	});
}

function initGroupSelector(){
	$('#group-selector select').change(function(event){
		var group = $(this).val();

		if (group){
			$.cookie('current_group', group, {'path':'/', 'expires':365});
		}
		else{
			$.removeCookie('current_group',{'path':'/'});
		}

		location.reload(true);

		return true;
	});
}

function initDateFields(){

	// $('.dateinput').after('<span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>');
	$('input.dateinput').datetimepicker({
		'format':'YYYY-MM-DD',
		locale: 'uk'
	});

	$('input.datetimeinput').datetimepicker({
		'format':'YYYY-MM-DD H:mm',
		locale: 'uk'
	});
}

function initEditPage(){
	$('a.edit-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url':link.attr('href'),
			'dataType':'html',
			'type':'get',
			'success': function(data, status, xhr){
				if(status!='success'){
					alert('Помилка на сервері. Спробуйте будь-ласка пізніше');
					return false;
				}
				// update modal window with arrived content from server
				var modal = $('#myModal'),
				html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-columns h2').text());
				modal.find('.modal-body').html(form);

				// init our edit form

				initEditForm(form, modal);

				//setup and show modal finally
				modal.modal('show');
			},
			'error':function(){
				alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
				return false;
			}
		});

		return false;
	});
}

function initEditForm(form, modal){
	initDateFields();

	modal.modal({
		'keyboard':false,
		'backdrop':false,
		'show':true,
	});

	//close modal window on Cancel button clcik
	form.find('input[name="cancel_button"]').click(function(event){
		modal.modal('hide');
		return false;
	});

	//make form work in AJAX form

	form.ajaxForm({
		'dataType':'html',
		'error':function(){
			alert('Помилка на сервері. Спробуйте будь-ласка пізніше');
			return false;
		},
		'success': function(data, status, xhr){
			var html = $(data), newform = html.find('#content-column form');

			modal.find('.modal-body').html(html.find('.alert'));

			if (newform.legth > 0 ){
				modal.find('.modal-body').append(newform);

				initEditPage(newform, modal);
			}
			else{
				setTimeout(function(){location.reload(true);}, 500);
			}

		}
	});
}

$(document).ready(function(){
	initJournal();
	initGroupSelector();
	initDateFields();
	initEditPage();
	
});