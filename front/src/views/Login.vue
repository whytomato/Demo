<template>
    <div class="bigBox">
        <div class="box" ref="box">
            <div class="pre-box">
                <h1>WELCOME</h1>
                <p>JOIN US!</p>
                <div class="img-box">
                    <img src="../assets/waoku.jpg" alt="" id="avatar" />
                </div>
            </div>
            <div class="register-form">
                <div class="title-box">
                    <h1>注册</h1>
                </div>
                <el-form ref="registerFormRef" :model="registerForm" label-with="5px">
                    <el-form-item prop="username" label=" ">
                        <el-input type="text" placeholder="用户名" v-model="registerForm.username" />
                    </el-form-item>
                    <el-form-item prop="password" label=" ">
                        <el-input type="password" placeholder="密码" v-model="registerForm.password" />
                    </el-form-item>
                    <el-form-item prop="confirmPassword" label=" ">
                        <el-input type="password" placeholder="确认密码" v-model="registerForm.confirmPassword" />
                    </el-form-item>

                </el-form>
                <div class="btn-box">
                    <button @click="register">注册</button>
                    <div class="p-container">
                        <!-- 绑定点击事件 -->
                        <p @click="inputEmail">验证邮箱?去填写</p>
                        <p @click="mySwitch">已有账号?去登录</p>
                    </div>

                </div>
            </div>
            <!-- 登录盒子 -->
            <div class="login-form">
                <!-- 标题盒子 -->
                <div class="title-box">
                    <h1>登录</h1>
                </div>
                <!-- 输入框盒子 -->
                <el-form ref="loginFormRef" :model="loginForm" label-with="5px">
                    <el-form-item prop="username" label=" ">
                        <el-input type="text" placeholder="用户名" v-model="loginForm.username" />
                    </el-form-item>
                    <el-form-item prop="password" label=" ">
                        <el-input type="password" placeholder="密码" v-model="loginForm.password" />
                    </el-form-item>
                </el-form>
                <!-- 按钮盒子 -->
                <div class="btn-box">
                    <button @click="login">登录</button>
                    <!-- 绑定点击事件 -->
                    <p @click="mySwitch">没有账号?去注册</p>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
/* 去除input的轮廓 */
input {
    outline: none;
}

.bigBox {
    /* 溢出隐藏 */
    height: 100vh;
    overflow-x: hidden;
    display: flex;
    /* 渐变方向从左到右 */
    background: linear-gradient(to right, rgb(247, 209, 215), rgb(191, 227, 241));
}

/* 最外层的大盒子 */
.box {
    width: 1050px;
    height: 600px;
    display: flex;
    /* 相对定位 */
    position: relative;
    z-index: 2;
    margin: auto;
    /* 设置圆角 */
    border-radius: 8px;
    /* 设置边框 */
    border: 1px solid rgba(255, 255, 255, 0.6);
    /* 设置盒子阴影 */
    box-shadow: 2px 1px 19px rgba(0, 0, 0, 0.1);
}

/* 滑动的盒子 */
.pre-box {
    /* 宽度为大盒子的一半 */
    width: 50%;
    height: 100%;
    /* 绝对定位 */
    position: absolute;
    /* 距离大盒子左侧为0 */
    left: 0;
    /* 距离大盒子顶部为0 */
    top: 0;
    z-index: 99;
    border-radius: 4px;
    background-color: #edd4dc;
    box-shadow: 2px 1px 19px rgba(0, 0, 0, 0.1);
    /* 动画过渡，先加速再减速 */
    transition: 0.5s ease-in-out;
}

/* 滑动盒子的标题 */
.pre-box h1 {
    margin-top: 150px;
    text-align: center;
    /* 文字间距 */
    letter-spacing: 5px;
    color: white;
    /* 禁止选中 */
    user-select: none;
    /* 文字阴影 */
    text-shadow: 4px 4px 3px rgba(0, 0, 0, 0.1);
}

/* 滑动盒子的文字 */
.pre-box p {
    height: 30px;
    line-height: 30px;
    text-align: center;
    margin: 20px 0;
    /* 禁止选中 */
    user-select: none;
    font-weight: bold;
    color: white;
    text-shadow: 4px 4px 3px rgba(0, 0, 0, 0.1);
}

/* 图片盒子 */
.img-box {
    width: 200px;
    height: 200px;
    margin: 20px auto;
    /* 设置为圆形 */
    border-radius: 50%;
    /* 设置用户禁止选中 */
    user-select: none;
    overflow: hidden;
    box-shadow: 4px 4px 3px rgba(0, 0, 0, 0.1);
}

/* 图片 */
.img-box img {
    width: 100%;
    transition: 0.5s;
}

/* 登录和注册盒子 */
.login-form,
.register-form {
    flex: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    /* 在垂直方向上居中对齐 */
}


/* 标题 */
.title-box h1 {
    text-align: center;
    color: white;
    /* 禁止选中 */
    user-select: none;
    letter-spacing: 5px;
    text-shadow: 4px 4px 3px rgba(0, 0, 0, 0.1);
}

/* 输入框盒子 */
.el-form {
    display: flex;
    /* 纵向布局 */
    flex-direction: column;
    /* 水平居中 */
    align-items: center;
}

.el-form-item {
    width: 65%;
}

/* 输入框 */
input {
    /* width: 60%; */
    height: 40px;
    margin-bottom: 20px;
    text-indent: 10px;
    border: 1px solid #fff;
    background-color: rgba(255, 255, 255, 0.3);
    border-radius: 120px;
    /* 增加磨砂质感 */
    backdrop-filter: blur(10px);
}

input:focus {
    /* 光标颜色 */
    color: #b0cfe9;
}

/* 聚焦时隐藏文字 */
input:focus::placeholder {
    opacity: 0;
}

/* 按钮盒子 */
.btn-box {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* 按钮 */
button {
    width: 100px;
    height: 30px;
    margin: 0 7px;
    line-height: 30px;
    border: none;
    border-radius: 4px;
    background-color: #69b3f0;
    color: white;
}

/* 按钮悬停时 */
button:hover {
    /* 鼠标小手 */
    cursor: pointer;
    /* 透明度 */
    opacity: 0.8;
}

/* 按钮文字 */
.btn-box p {

    /* 禁止选中 */
    user-select: none;
    font-size: 14px;
    color: white;
}

.btn-box p:hover {
    cursor: pointer;
    border-bottom: 1px solid white;
}

.p-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    line-height: 0.7;
}
</style>
<script setup>
import { getCurrentInstance, reactive } from 'vue';
import { ref } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'
let flag = ref(true)
let countdown = 10;
const registerForm = reactive({
    username: '',
    password: '',
    confirmPassword: ''
});
const loginForm = reactive({
    username: '',
    password: ''
})

const emaildata = reactive({
    isEmail: false,
    countdown: 0,
    address: '',
    verification_code: ''

})

// 在这里可以进行初始化操作

const mySwitch = () => {
    const pre_box = document.querySelector('.pre-box')
    const img = document.querySelector("#avatar")
    if (flag.value) {
        pre_box.style.transform = "translateX(100%)"
        pre_box.style.backgroundColor = "#c9e0ed"
        img.src = require("@/assets/wuwu.jpeg")
    }
    else {
        pre_box.style.transform = "translateX(0%)"
        pre_box.style.backgroundColor = "#edd4dc"
        img.src = require("@/assets/waoku.jpg")
    }
    flag.value = !flag.value
}

const register = () => {
    let data = new FormData()
    if (registerForm.username == '') {
        Swal.fire('注册失败!',
            '请输入用户名！',
            'error')
        return
    }
    if (/\s/.test(registerForm.username)) {
        Swal.fire('注册失败!',
            '用户名中不能存在空格！',
            'error')
        return
    }
    if (/\s/.test(registerForm.password) || /\s/.test(registerForm.confirmPassword)) {
        Swal.fire('注册失败!',
            '密码中不能存在空格！',
            'error')
        return
    }
    if (registerForm.password == '' || registerForm.confirmPassword == '') {
        Swal.fire('注册失败!',
            '请输入密码！',
            'error')
        return
    }
    data.append("username", registerForm.username)
    data.append("password_1", registerForm.password)
    data.append("password_2", registerForm.confirmPassword)
    // if (this.isEmail) {
    //     data.append("email", this.emailaddress)
    //     data.append("verification_code", this.verification_code)
    // }
    if (emaildata.isEmail) {
        data.append("email", emaildata.address)
        data.append("verification_code", emaildata.verification_code)

    }
    data.append("isEmail", emaildata.isEmail)
    // data.append("isEmail", "false")
    axios.post('/api/publish/register', data)
        .then(response => {
            switch (response.data.errno) {
                case 0:
                    Swal.fire('恭喜!',
                        '你已经注册成功！',
                        'success')
                    break;
                case 1001:
                    Swal.fire('ERROR!',
                        '请求方式错误！',
                        'error')
                    break;
                case 1002:
                    Swal.fire('注册失败!',
                        '用户名重复，请重试！',
                        'warning')
                    break;
                case 1003:
                    Swal.fire('注册失败!',
                        '两次输入的密码不同，请重试！',
                        'warning')
                    break;
                case 1004:
                    Swal.fire('注册失败', response.data.msg, 'error')
                    break;
                case 1005:
                    Swal.fire('注册失败', response.data.msg, 'error')
                    break;
                case 1006:
                    Swal.fire('注册失败', response.data.msg, 'error')
                    break;
                default:
                    break;
            }
        })
}
const inputEmail = async () => {
    emaildata.isEmail = true
    const { value: email } = await Swal.fire({
        title: '请输入邮箱',
        input: 'email',
        inputLabel: '你的邮箱地址',
        inputPlaceholder: '输入你的邮箱地址',
        confirmButtonText: '发送验证码',
        preConfirm: (inputValue) => {
            emaildata.address = inputValue;
            console.log(emaildata.address)
        }
    })

    if (email) {
        // Swal.fire(`Entered email: ${email}`)
        sendCode();
    }
}
const sendCode = () => {
    // if (!this.isEmailValid(this.emailaddress)) {
    //     Swal.fire('发送失败', '请输入有效的邮箱地址！', 'error')
    //     return
    // }
    let data = new FormData()
    data.append('email', emaildata.address)
    if (emaildata.countdown === 0) {
        emaildata.countdown = 10;
        // this.updateButtonText();

        // const timer = setInterval(() => {
        //     if (this.countdown > 0) {
        //         this.countdown--;
        //         this.updateButtonText();
        //     } else {
        //         clearInterval(timer);
        //     }
        // }, 1000); // 每秒更新倒计时时间
    }
    axios.post('/api/publish/sendcode', data)
        .then(response => {
            showSwalWithCountdown()
            console.log('发送成功')
        }).catch(error => {
            console.error('发送失败')
        })
}

let isResendButtonDisabled = false;
const startCountdown = () => {
    const resendButton = Swal.getCancelButton();
    resendButton.disabled = true
    const timer = setInterval(() => {
        if (countdown > 0) {
            countdown--;
            // const cancelButtonText = countdown > 0 ? `重新发送 (${countdown}s)` : `重新发送`;
            Swal.update({
                allowOutsideClick: false,
                cancelButtonText: `重新发送 (${countdown}s)`,
                showCancelButton: true,
                // cancelButtonColor: isResendButtonDisabled ? '#999999' : '',

            });
        } else {
            clearInterval(timer);
            resendButton.disabled = false,
                Swal.update({

                    showCancelButton: true,
                    cancelButtonText: `重新发送`
                })
        }
    }, 1000);
};

const showSwalWithCountdown = () => {
    Swal.fire({
        title: '输入验证码',
        input: 'text',
        inputLabel: '验证码',
        inputPlaceholder: '输入你的验证码',
        showCancelButton: true,
        confirmButtonText: '注册',
        cancelButtonText: `重新发送 (${countdown}s)`,
        allowOutsideClick: false,
        preConfirm: (inputValue) => {
            emaildata.verification_code = inputValue
            // 处理注册逻辑
        }
    }).then((result) => {
        if (result.isConfirmed) {
            register()
            // 处理注册逻辑
        } else if (result.dismiss === Swal.DismissReason.cancel) {
            countdown = 10
            showSwalWithCountdown()
            // 处理重新发送逻辑
        }
    });
    startCountdown();
};


const login = () => {
    let data = new FormData()
    if (loginForm.username == '') {
        Swal.fire('登录失败!',
            '请输入用户名！',
            'error')
        return
    }
    if (loginForm.password == '') {
        Swal.fire('登录失败!',
            '请输入密码！',
            'error')
        return
    }
    data.append("username", loginForm.username)
    data.append("password", loginForm.password)
    axios.post('/api/publish/login', data).then(response => {
        switch (response.data.errno) {
            case 0:
                Swal.fire('恭喜!',
                    '你已经登录成功！',
                    'success')
                break;
            case 1001:
                Swal.fire('ERROR!',
                    '请求方式错误！',
                    'error')
                break;
            case 1002:
                Swal.fire('登录失败!',
                    '用户不存在，请重试！',
                    'warning')
                break;
            case 1003:
                Swal.fire('登录失败!',
                    '输入的密码不正确，请重试！',
                    'error')
                break;
            case 1004:
                Swal.fire('ERROR!',
                    '不能重复登录！',
                    'error')
                break;
            default:
                break;
        }
    })

}
</script>
