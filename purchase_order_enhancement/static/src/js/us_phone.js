odoo.define('purchase_order_us_phone', function (require) {
    "use strict";
    
        let FieldChar = require('').FieldChar;
        let registry = require('web.field_registry');    

        let USPhoneNumber = FieldChar.extend({
            events: _.extend({}, FieldChar.prototype.events, {
                'keyUp': '_onKeyUp',
            }),
            _onKeyUp: function(){
                
            }
        });
        registry.add("us_phone_number", USPhoneNumber)
})