const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value //get token itself
const alertBox = document.getElementById('alert-box')

const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
        ${msg}
    </div>
    `
}

Dropzone.autoDiscover = false
const myDropzone = new Dropzone('#my-dropzone', {
    url: '/reports/upload/',
    init: function () {
        this.on('sending', function (file, xhr, formData) {
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
        })
        this.on('success', function (file, response) {
            console.log(response.ex)
            if (response.ex) {
                handleAlerts('warning', 'Ficheiro já existe!')
            } else {
                handleAlerts('success', 'O ficheiro foi adicionado!')
            }
        })
    },
    maxFiles: 5,
    maxFilesize: 3,
    acceptedFiles: '.csv'
})