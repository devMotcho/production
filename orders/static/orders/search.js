const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')
const modalBody = document.getElementById('modal-body')
const reportForm = document.getElementById('report-form')
const alertBox = document.getElementById('alert-box')

const reportName = document.getElementById('id_name')
const reportText = document.getElementById('id_text')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value


const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
    <div class="alert alert-${type} role="alert">
    ${msg}
    <div>
    `
}

if (img) {
    reportBtn.classList.remove('not-visible');
}

reportBtn.addEventListener('click', () => {
    console.log('clicked')
    img.setAttribute('class', 'w-100')
    modalBody.prepend(img)

    console.log(img.src)

    reportForm.addEventListener('submit', e => {
        e.preventDefault()

        const formData = new FormData()
        formData.append('csrfmiddlewaretoken', csrf)
        formData.append('name', reportName.value)
        formData.append('text', reportText.value)
        formData.append('image', img.src)

        $.ajax({
            type: 'POST',
            url: '/reports/create-report/',
            data: formData,
            success: function (response) {
                console.log(response)
                handleAlerts('success', 'Relatório Submetido')
            },
            error: function (error) {
                console.log(error)
                handleAlerts('danger', 'Erro ao Submeter Relatório! ')
            },

            processData: false,
            contentType:false,
        })
    })
})