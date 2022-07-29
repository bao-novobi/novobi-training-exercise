odoo.define('purchase_order_enhancement.purchase_order_us_phone', function (require) {
    "use strict";
    
        let FieldChar = require('web.basic_fields').FieldChar;
        let registry = require('web.field_registry');    


        let USPhoneNumber = FieldChar.extend({
            className: 'o_field_us_phone_number',
            events: _.extend({}, FieldChar.prototype.events, {'keyup': '_onKeyUp',}),
            fm: function(number){
                return "0"
            },
            _onKeyUp: function(e){
                let phone_number=this._getValue();
                let format_phone = this.fm(phone_number);
                this.$input.val(format_phone);
            }
        });
        registry.add("us_phone_number", USPhoneNumber)
        return USPhoneNumber
})