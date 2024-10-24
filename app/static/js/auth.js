document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => showTab(tab.dataset.tab));
});

function showTab(tabName) {
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.form').forEach(form => form.classList.remove('active'));

    document.querySelector(`.tab[data-tab="${tabName}"]`).classList.add('active');
    document.getElementById(`${tabName}Form`).classList.add('active');
}

const validateForm = fields => fields.every(field => field.trim() !== '');

const sendRequest = async (url, data) => {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            alert(result.message || 'Operation done!');
            return result;
        } else {
            alert(result.message || 'Query error!');
            return null;
        }
    } catch (error) {
        console.error("Error:", error);
        alert('Error on server');
    }
};

const handleFormSubmit = async (formType, url, fields) => {
    if (!validateForm(fields)) {
        alert('Пожалуйста, заполните все поля.');
        return;
    }

    const data = await sendRequest(url, formType === 'login'
        ? {email: fields[0], password: fields[1]}
        : {email: fields[0], name: fields[1], password: fields[2], password_check: fields[3]});

    if (data && formType === 'login') {
        window.location.href = '/chat';
    }
};

document.getElementById('loginButton').addEventListener('click', async (event) => {
    event.preventDefault();

    const email = document.querySelector('#loginForm input[type="email"]').value;
    const password = document.querySelector('#loginForm input[type="password"]').value;

    await handleFormSubmit('login', 'login/', [email, password]);
});

document.getElementById('registerButton').addEventListener('click', async (event) => {
    event.preventDefault();

    const email = document.querySelector('#registerForm input[type="email"]').value;
    const name = document.querySelector('#registerForm input[type="text"]').value;
    const password = document.querySelectorAll('#registerForm input[type="password"]')[0].value;
    const password_check = document.querySelectorAll('#registerForm input[type="password"]')[1].value;

    if (password !== password_check) {
        alert('Пароли не совпадают.');
        return;
    }

    await handleFormSubmit('register', 'register/', [email, name, password, password_check]);
});