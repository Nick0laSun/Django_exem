function wave_choice_f() {
    var choice = document.getElementById('wave').value;
    //document.getElementById("wave").oninput = function () {
    //    var inp = this.value;
    //    alert(inp);
    //}
    var tbody = document.getElementById('s_menu').getElementsByTagName('tr')[0];
    var td = tbody.getElementsByTagName('td')[2];
    var p = td.getElementsByTagName('p')[1];
    if (p) {
        //alert('not null');
        p.remove();
    }

    if (choice == "Поверхностная") {
        var box = document.createElement("p");
        box.innerHTML = '<label>Настройки волнопродуктора:</label><br>' +
                        '<input type="number" name="amplitude" placeholder="Амплитуда (См)"/><br>' +
                        '<input type="number" name="quantity" placeholder="Количество волн"/><br>' +
                        '<input type="number" name="frequency" placeholder="Частота волнопрод.(Гц)"/><br>' +
                        'Прод. работы (мин:сек)<input type="time" name="operatingtime"/><br>' +
                        '<input type="number" name="thickness" placeholder="Толщина слоя жидкости"/>';
        td.appendChild(box);
    }

    if (choice == "Внутренняя") {
        var box = document.createElement("p");
        box.innerHTML = '<p>' +
                            '<label>Настройки дамбы:</label><br>' +
                            '<input type="number" name="wall_coordinate" placeholder="Положение стенки"/><br>' +
                        '</p>' +
                        '<p>' +
                            '<label>Стратификация</label><br>' +
                            '<input list="d_layers_list" name="d_layers" id="d_layers">' +
                            '<datalist id="d_layers_list">' +
                                '<option value="1">Один слой</option>' +
                                '<option value="2">Два слоя</option>' +
                                '<option value="3">Три слоя</option>' +
                            '</datalist><br>' +
                            '<input type="button" onclick="d_layers_choice_f()" value="Подтвердить" />' +
                        '</p>';
        td.appendChild(box); 
    } 
}

function d_layers_choice_f() {
    var choice = document.getElementById('d_layers').value;

    var tbody = document.getElementById('s_menu').getElementsByTagName('tr')[0];
    var td = tbody.getElementsByTagName('td')[2];
    var p = td.getElementsByTagName('p')[1];
    var strat = p.getElementsByTagName('p')[2];
    if (strat) {
        strat.remove();
    }

    if (choice == "1") {
        var box = document.createElement("p");
        box.innerHTML = '<p>' +
                            '<label>Параметры жидкости:</label><br>' +
                            '<input type="number" name="dam_top_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_top_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_top_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>';
        p.appendChild(box); 
    }

    if (choice == "2") {
        var box = document.createElement("p");
        box.innerHTML = '<p>' +
                            '<label>Верхний слой:</label><br>' +
                            '<input type="number" name="dam_top_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_top_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_top_layer_color" placeholder="Название красителя"/><br>' + 
                        '</p>' +
                        '<p>' +
                            '<label>Нижний слой:</label><br>' +
                            '<input type="number" name="dam_lower_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_lower_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_lower_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>';
        p.appendChild(box);
    }

    if (choice == "3") {
        var box = document.createElement("p");
        box.innerHTML = '<p>' +
                            '<label>Верхний слой:</label><br>' +
                            '<input type="number" name="dam_top_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_top_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_top_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>' +
                        '<p>' +
                            '<label>Средний слой:</label><br>' +
                            '<input type="number" name="dam_middle_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_middle_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_middle_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>' +
                        '<p>' +
                            '<label>Нижний слой:</label><br>' +
                            '<input type="number" name="dam_lower_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_lower_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_lower_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>';
        p.appendChild(box);
    }
}

function layers_choice_f() {
    var choice = document.getElementById('layers').value;
    
    var tbody = document.getElementById('s_menu').getElementsByTagName('tr')[0];
    var td = tbody.getElementsByTagName('td')[1];
    var p = td.getElementsByTagName('p')[1];
    if (p) {
        p.remove();
    }
    
    if (choice == "1") {
        var box = document.createElement("p");
        box.innerHTML = '<p>' +
                            '<label>Параметры жидкости:</label><br>' +
                            '<input type="number" name="dam_top_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_top_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_top_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>';
        td.appendChild(box); 
    }

    if (choice == "2") {
        var box = document.createElement("p");
        box.innerHTML = '<p>' +
                            '<label>Верхний слой:</label><br>' +
                            '<input type="number" name="dam_top_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_top_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_top_layer_color" placeholder="Название красителя"/><br>' + 
                        '</p>' +
                        '<p>' +
                            '<label>Нижний слой:</label><br>' +
                            '<input type="number" name="dam_lower_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_lower_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_lower_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>';
        td.appendChild(box);
    }

    if (choice == "3") {
        var box = document.createElement("p");
        box.innerHTML = '<p>' +
                            '<label>Верхний слой:</label><br>' +
                            '<input type="number" name="dam_top_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_top_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_top_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>' +
                        '<p>' +
                            '<label>Средний слой:</label><br>' +
                            '<input type="number" name="dam_middle_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_middle_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_middle_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>' +
                        '<p>' +
                            '<label>Нижний слой:</label><br>' +
                            '<input type="number" name="dam_lower_layer_height" placeholder="Толщина"/><br>' +
                            '<input type="number" name="dam_lower_layer_density" placeholder="Плотность г/см^3"/><br>' +
                            '<input type="text" name="dam_lower_layer_color" placeholder="Название красителя"/><br>' +
                        '</p>';
        td.appendChild(box);
    }
}

function laser_choice_f() {
    var choice = document.getElementById('laser').value;
    
    var tbody = document.getElementById('s_menu').getElementsByTagName('tr')[0];
    var td = tbody.getElementsByTagName('td')[3];
    var p = td.getElementsByTagName('p')[1];
    if (p) {
        p.remove();
    }

    if (choice == "Использовался") {
        var box = document.createElement("p");
        box.innerHTML = 
                            '<input type="text" name="laser_video" placeholder="Сылка на видео"/><br>' +
                            '<input type="number" name="laser_coordinate" placeholder="Место размещения"/><br>' +
                            '<input type="number" name="laser_angle" placeholder="Угол линзы"/><br>';
        td.appendChild(box);
    }
}

function extra_settings_choice_f() {
    var choice = document.getElementById('ex_sett').value;
    
    var tbody = document.getElementById('s_menu').getElementsByTagName('tr')[0];
    var td = tbody.getElementsByTagName('td')[4];
    var p = td.getElementsByTagName('p')[1];
    if (p) {
        p.remove();
    }

    if (choice == "Есть") {
        var box = document.createElement("p");
        box.innerHTML = '<p>' +
                            'Препятствие:<br>' +
                            '<input type="number" name="obstacle_coordinate" placeholder="Место размещения"/><br>' +
                            '<input type="number" name="obstacle_height" placeholder="Высота препятствия"/><br>' +
                        '</p>' +
                        '<p>' +
                            '<label>Тип частиц на поверхности жидкости:</label><br>' +
                            '<input type="text" name="type_of_particles"/>' +
                        '</p>';
        td.appendChild(box);
    }
}

function create_smenu_f() {
    var menu = document.getElementById('search_menu_place');
    var p = menu.getElementsByTagName('p')[0];
    if (p) {
        p.remove();
    } else {
        var box = document.createElement('p');
        box.innerHTML = '<form name="test_search" method="POST" action="test_search">' +
                            '{% csrf_token %}' +
                            '<h3>Поиск эксперимента</h3>' +
                            '<table id="s_menu">' +
                            '<tbody>' +
                                '<tr>' +
                                '<td>' +
                                    '<p>' +
                                        '<label>Id:</label><br>' +
                                        '<input type="number" name="id" />' +
                                    '</p>' +
                                    '<p>' +
                                        '<label>Дата и время проведения:</label><br>' +
                                        '<input type="datetime-local" name="datetime" />' +
                                    '</p>' +
                                    '<p>' +
                                        '<label>Длительность эксперимента:</label><br>' +
                                        '<input type="time" name="duration_of_exp" />' +
                                    '</p>' +
                                    '<p>' +
                                        '<label>Название эксперимента:</label><br>' +
                                        '<input type="text" name="title" />' +
                                    '</p>' +
                                    '<p>' +
                                        '<label>Тип берега:</label><br>' +
                                        '<input type="text" name="bottom" />' +
                                    '</p>' +
                                    '<p>' +
                                        '<label>Полярность волны:</label><br>' +
                                        '<input type="text" name="polarity"/>' +
                                    '</p>' +
                                '</td>' +
                                '<td>' +
                                    '<p>' +
                                    '<label>Стратификация:</label><br>' +
                                    '<input list="layers_list" name="layers" id="layers">' +
                                    '<datalist id="layers_list">' +
                                        '<option value="1">Один слой</option>' +
                                        '<option value="2">Два слоя</option>' +
                                        '<option value="3">Три слоя</option>' +
                                    '</datalist><br>' +
                                    '<input type="button" onclick="layers_choice_f()" value="Подтвердить" />' +
                                    '</p>' +
                                '</td>' +
                                '<td>' +
                                    '<p>' +
                                        '<label>Тип волны:</label><br>' +
                                        '<input list="wave_list" name="wave" id="wave">' +
                                        '<datalist id="wave_list">' +
                                            '<option value="Поверхностная"></option>' +
                                            '<option value="Внутренняя"></option>' +
                                        '</datalist><br>' +
                                        '<input type="button" onclick="wave_choice_f()" value="Подтвердить" />' +
                                    '</p>' +
                                '</td>' +
                                '<td>' +
                                    '<p>' +
                                        '<label>Лазер:</label><br>' +
                                        '<input list="laser_list" name="laser" id="laser">' +
                                        '<datalist id="laser_list">' +
                                            '<option value="Использовался"></option>' +
                                            '<option value="Не использовался"></option>' +
                                        '</datalist><br>' +
                                        '<input type="button" onclick="laser_choice_f()" value="Подтвердить" />' +
                                    '</p>' +
                                '</td>' +
                                '<td>' +
                                    '<p>' +
                                        '<label>Доп. настройки:</label><br>' +
                                        '<input list="extra_settings" name="ex_sett" id="ex_sett">' +
                                        '<datalist id="extra_settings">' +
                                            '<option value="Есть"></option>' +
                                            '<option value="Нет"></option>' +
                                        '</datalist><br>' +
                                        '<input type="button" onclick="extra_settings_choice_f()" value="Подтвердить"/>' +
                                    '</p>' +
                                '</td>' +
                            '</tr>' +
                            '</tbody>' +
                            '</table>' +
                            '<input type="submit" value="Поиск" >' +
                        '</form>';
        menu.append(box);
    }
}