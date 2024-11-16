let form = document.querySelector('form')
let data_container = document.querySelector('.data-list')
let inputs = document.querySelectorAll('input')


function auto_focus() {
    // 网页加载后, 自动聚焦到输入框
    inputs.forEach(input => {
        if (input.name === "num1") input.focus()
    })
}


function clearInputs() {
    inputs.forEach(input => {
        if (input.name.indexOf('num') !== -1) {
            input.value = ''
        }
    })
}

function dataSubmit() {
    let data = new FormData(this)
    console.log(data)

    fetch('/golden_point/', {method: 'post', body: data})
        .then(async res => {
            let lists = await res.json()

            let entries = Object.entries(lists);
            entries = entries.sort()

            // 删除pre 的子节点
            data_container.removeChild(data_container.firstChild);

            let div = document.createElement('div')
            data_container.appendChild(div)

            entries.forEach(entry => {
                let span = document.createElement('span')
                let value = document.createElement('span')

                span.classList.add('key')
                span.textContent = entry[0] + " -> "

                value.classList.add('value')
                value.textContent = entry[1]

                div.appendChild(span)
                div.appendChild(value)
                div.appendChild(document.createElement('br'))
            })

        })
        .catch((error) => {
            console.log(error)
        })

    auto_focus()
    clearInputs()
    return false;
}

form.addEventListener('submit', dataSubmit)
auto_focus()
