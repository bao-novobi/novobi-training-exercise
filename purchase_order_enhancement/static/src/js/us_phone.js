odoo.define('purchase_order_enhancement.purchase_order_us_phone', function (require) {
    "use strict";

    let FieldChar = require('web.basic_fields').FieldChar;
    let registry = require('web.field_registry');


    let USPhoneNumber = FieldChar.extend({
        className: 'o_field_us_phone_number',
        events: _.extend({}, FieldChar.prototype.events, { 'focusout': '_onFocusOut', }),
        format_phone_number: function (number) {
            let formatted_number = number.replace(/\D/g, "")
            let number_len = formatted_number.length
            if (number_len > 3){
                formatted_number = formatted_number.slice(0, 3) + "-" + formatted_number.slice(3)
            }
            return formatted_number;
        },
        _onFocusOut: function (e) {
            let phone_number = this._getValue();
            let formated_phone_number = this.format_phone_number(phone_number);
            this.$input.val(formated_phone_number);
        }
    });
    registry.add("us_phone_number", USPhoneNumber);
    return USPhoneNumber;
})