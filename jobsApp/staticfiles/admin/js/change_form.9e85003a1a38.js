/*global showAddAnotherPopup, showRelatedObjectLookupPopup showRelatedObjectPopup updateRelatedObjectLinks*/

(function($) {
    'use strict';
    $(document).ready(function() {
        document.getElementById("id_residence_place").style.display = 'none';
        document.getElementById('id_lang_set-0-lang_type').selectedIndex=1;
        var modelName = $('#django-admin-form-add-constants').data('modelName');
        $('body').on('click', '.add-another', function(e) {
            e.preventDefault();
            var event = $.Event('django:add-another-related');
            $(this).trigger(event);
            if (!event.isDefaultPrevented()) {
                showAddAnotherPopup(this);
            }
        });

        if (modelName) {
            $('form#' + modelName + '_form :input:visible:enabled:first').focus();
        }
    });
})(django.jQuery);
