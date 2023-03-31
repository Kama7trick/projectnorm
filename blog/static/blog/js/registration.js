$(document).ready(function () {
        $('#registration_form').bootstrapValidator({
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                name: {
                    validators: {
                        stringLength: {
                            min: 3,
                            message: 'Please enter atleast 3 characters'
                        },
                        notEmpty: {
                            message: 'Please enter  your name'
                        }
                    }
                },
                email: {
                    validators: {
                        notEmpty: {
                            message: 'Please enter your email address'
                        },
                        emailAddress: {
                            message: 'Please enter a valid email address'
                        }
                    }
                },
                password: {
                    validators: {
                        stringLength: {
                            min: 8,
                            message: 'Please enter at least 8 characters and no more than 16',
                            max: 16
                        },
                        identical: {
                            field: 'confirmpassword',
                            message: 'The password and the confirm password are not the same'
                        },
                        notEmpty: {
                            message: 'Please enter your password'
                        }

                    }
                },
                confirmpassword: {
                    validators: {
                        notEmpty: {
                            message: 'Please confirm your password'
                        },
                        identical: {
                            field: 'password',
                            message: 'The password and the confirm password are not the same'
                        }

                    }
                }

            },
            submitHandler: function(validator, form) {
                $('#registration_success').slideDown({ opacity: "show" }, "slow");
                $.post(form.attr('action'),form.serialize(),
                    function() {

                    },
                    'json');
            }
        });

    });