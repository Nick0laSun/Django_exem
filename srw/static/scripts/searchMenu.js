$(window).scroll(function() {
    alert('It is work');
});

window.onload = function () {
    console.log('It is work');
};

alert('JS is on');

$(document).ready(function (){
    console.log('JS is on');

    function test_click() {
        console.log('click');
    }

    function change_query_field_f(this) {
        var query_field = this.getElementById('input_field');
        var value = select.options[select.selectedIndex].value;
        var input = query_field.getElementsByTagName('input')[0];
        if (input) {input.remove();}
        
        alert(value);

        if(value == "id") {
            query_field.innerHTML = '<input type="number" name="id_field" placeholder="id эксперимента"/>';
        }
    }
});