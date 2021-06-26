function expand(id,elem){
    let arrow = document.getElementById(elem); 
    let task = document.getElementById(id);
    if(task.style.display === 'none'){
        task.style.display = "initial";    
    }
    else{
        task.style.display = "none";    
    }
    arrow.classList.toggle("arrow-active");
}



// falta borrar boton comenzar // podria crear con datos devueltos en un json una nueva tarjeta en_proceso en lugar de usar las primeras
function start_task(task_id){
    $.ajax({
        url : `/tasks/${task_id}/start/`,
        type : "POST",
        dataType: 'json',
        success: function(data){
            var card = `<div class="card mb-3 glasseffect1" style="max-width: 18rem;width:18rem;" id="id-${task_id}">
                            <div class="card-header">
                                ${data.title}
                                <a href="/tasks/${task_id}/delete/" class="btn btn-sm btn-danger ms-2 float-end fw-bold text-dark">
                                    &times;
                                </a>
                                <a href="/tasks/${task_id}/update/" class="btn btn-sm btn-secondary ms-2 float-end fw-bold text-dark">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-pen" viewBox="0 0 16 16">
                                            <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001zm-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708l-1.585-1.585z"/>
                                        </svg>
                                    </a>
                                <a onclick="expand('${task_id}','arrow-${task_id}')" class="btn btn-sm btn-info float-end fw-bold arrow" id="arrow-${task_id}">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" fill="currentColor" class="bi bi-caret-down-fill" viewBox="0 0 16 16">
                                        <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
                                    </svg>
                                </a>
                            </div>
                            <div class="card-body" id="${task_id}" style="display: none;">
                                <h5 class="card-title">${data.subtitle}</h5>
                                <p class="card-text">${data.description}</p>                             
                                <p class="card-text">Fecha: ${data.limit_date}</p>
                                <a onclick="end_task('${task_id}')" class="btn btn-warning">Finalizar</a>
                            </div>
                        </div>`;
            $(`#inProcess`).prepend(card);
            $(`#id-${task_id}`).remove();
            expand(task_id,`arrow-${task_id}`);
        },
        error: function(err){
            console.log(err);
        }
    });
}

//quitar el boton finalizar, hacer lo mismo que arriba
function end_task(task_id){
    $.ajax({
        url : `/tasks/${task_id}/end/`,
        type : "POST",
        dataType : 'json',
        success: function(data){
            var card = `<div class="card mb-3 glasseffect1" style="max-width: 18rem;width:18rem;">
                            <div class="card-header">
                                ${data.title}
                                <a href="/tasks/${task_id}/delete/" class="btn btn-sm btn-danger ms-2 float-end fw-bold text-dark">
                                    &times;
                                </a>
                                <a href="/tasks/${task_id}/update/" class="btn btn-sm btn-secondary ms-2 float-end fw-bold text-dark">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-pen" viewBox="0 0 16 16">
                                        <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001zm-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708l-1.585-1.585z"/>
                                    </svg>
                                </a>
                                <a onclick="expand('${task_id}','arrow-${task_id}')" class="btn btn-sm btn-info float-end fw-bold arrow" id="arrow-${task_id}">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" fill="currentColor" class="bi bi-caret-down-fill" viewBox="0 0 16 16">
                                        <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
                                        </svg>
                                </a>
                            </div>
                            <div class="card-body" id="${task_id}" style="display: none;">
                                <h5 class="card-title">${data.subtitle}</h5>
                                <p class="card-text">${data.description}</p>
                                <p class="card-text">Fecha: ${data.limit_date}</p>
                            </div>
                        </div>`;
            $(`#taskEnded`).prepend(card);
            $(`#id-${task_id}`).remove();
            expand(task_id,`arrow-${task_id}`);
        },
        error: function(err){
            console.log(err);
        }
    });
}