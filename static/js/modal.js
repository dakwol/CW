 $(document).ready(function() {
            $(function() {
                $( "#some_flag" ).dialog({
                    modal: true,
                    closeOnEscape: false,
                    dialogClass: "no-close",
                    resizable: false,
                    draggable: false,
                    width: 600,
                    buttons: [
                        {
                            text: "OK",
                            click: function() {
                            $( this ).dialog( "close" );
                            }
                        }
                    ]
                });
            });
        });