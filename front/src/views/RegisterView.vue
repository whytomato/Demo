<template>
    <el-input v-model="username" placeholder="Please input" />
    <el-input v-model="password_1" placeholder="Please input" type="password" show-password @input="handleInput1($event)" />
    <el-input v-model="password_2" placeholder="Please input" type="password" show-password @input="handleInput2($event)" />
    <el-input v-model="emailaddress" placeholder="Please input" />

    <el-button type="success" @click="send">register</el-button>
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
            data.append("username", this.username)
            data.append("password_1", this.password_1)
            data.append("password_2", this.password_2)
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
                        default:
                            break;
                    }
                })
        },

        handleInput1(event) {
            // const input = event.target.value;
            // const filteredInput = input.replace(/\s/g, '');
            const filteredInput = event.trim();
            this.password_1 = filteredInput;
        },
        handleInput2(event) {
            // const input = event.target.value;
            // const filteredInput = input.replace(/\s/g, '');
            const filteredInput = event.trim();
            this.password_2 = filteredInput;
        },
        handleKeyDown(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                this.send();
            }
        }
    }
}
</script>
