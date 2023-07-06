<template>
    <el-input v-model="username" placeholder="Please input" />
    <el-input v-model="password_1" placeholder="Please input" type="password" show-password @input="handleInput1($event)" />
    <el-input v-model="password_2" placeholder="Please input" type="password" show-password @input="handleInput2($event)" />

    <div v-if="isEmail">
        <el-input v-model="emailaddress" placeholder="email" />
        <el-input v-model="verification_code" placeholder="verification_code" />
    </div>
    <el-switch v-model="isEmail" />
    <el-button type="success" @click="send">register</el-button>
    <el-button type="primary" :disabled="countdown > 0" @click="sendCode">{{ buttonText }}</el-button>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'

export default {
    data() {
        return {
            username: '',
            password_1: '',
            password_2: '',
            emailaddress: '',
            countdown: 0,
            buttonText: '发送',
            verification_code: '',
            isEmail: true
        }
    },
    mounted() {
        document.addEventListener('keydown', this.handleKeyDown);
    },
    destroyed() {
        document.removeEventListener('keydown', this.handleKeyDown)
    },
    methods: {
        send() {
            let data = new FormData()
            if (this.username == '') {
                Swal.fire('注册失败!',
                    '请输入用户名！',
                    'error')
                return
            }
            if (/\s/.test(this.username)) {
                Swal.fire('注册失败!',
                    '用户名中不能存在空格！',
                    'error')
                return
            }
            if (/\s/.test(this.password_1) || /\s/.test(this.password_2)) {
                Swal.fire('注册失败!',
                    '密码中不能存在空格！',
                    'error')
                return
            }
            if (this.password_1 == '' || this.password_2 == '') {
                Swal.fire('注册失败!',
                    '请输入密码！',
                    'error')
                return
            }
            if (this.isEmail) {
                if (!this.emailaddress) {
                    Swal.fire('注册失败', '请输入有效的邮箱地址！', 'error')
                    return
                }
                if (!this.isEmailValid(this.emailaddress)) {
                    Swal.fire('注册失败', '请输入有效的邮箱地址！', 'error')
                    return
                }
            }
            data.append("username", this.username)
            data.append("password_1", this.password_1)
            data.append("password_2", this.password_2)
            if (this.isEmail) {
                data.append("email", this.emailaddress)
                data.append("verification_code", this.verification_code)
            }
            data.append("isEmail", this.isEmail)
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
        },
        sendCode() {
            if (!this.isEmailValid(this.emailaddress)) {
                Swal.fire('发送失败', '请输入有效的邮箱地址！', 'error')
                return
            }
            let data = new FormData()
            data.append('email', this.emailaddress)
            if (this.countdown === 0) {
                this.countdown = 10;
                this.updateButtonText();

                const timer = setInterval(() => {
                    if (this.countdown > 0) {
                        this.countdown--;
                        this.updateButtonText();
                    } else {
                        clearInterval(timer);
                    }
                }, 1000); // 每秒更新倒计时时间
            }
            axios.post('/api/publish/sendcode', data)
                .then(response => {
                    console.log('发送成功')
                }).catch(error => {
                    console.error('发送失败')
                })
        },
        startCountdown() {
            if (this.countdown === 0) {
                this.countdown = 30; // 设置倒计时时间为两分钟（120秒）
                this.updateButtonText();

                const timer = setInterval(() => {
                    if (this.countdown > 0) {
                        this.countdown--;
                        this.updateButtonText();
                    } else {
                        clearInterval(timer);
                    }
                }, 1000); // 每秒更新倒计时时间
            }
        },
        updateButtonText() {
            if (this.countdown > 0) {
                this.buttonText = `${this.countdown} 秒后重新发送`;
            } else {
                this.buttonText = '重新发送';
            }
        },
        handleInput1(event) {
            const filteredInput = event.trim();
            this.password_1 = filteredInput;
        },
        handleInput2(event) {
            const filteredInput = event.trim();
            this.password_2 = filteredInput;
        },
        handleKeyDown(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                this.send();
            }
        },
        isEmailValid(email) {
            const pattern = /^[\w.-]+@[\w.-]+\.\w+$/
            return pattern.test(email)
        }
    }
}
</script>
