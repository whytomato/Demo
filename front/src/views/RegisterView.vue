<template>
    <el-input v-model="username" placeholder="Please input" />
    <el-input v-model="password_1" placeholder="Please input" />
    <el-input v-model="password_2" placeholder="Please input" />
    <el-button type="success" @click="send">register</el-button>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            username: '',
            password_1: '',
            password_2: ''
        }
    },
    methods: {
        send() {

            let data = new FormData()
            data.append("username", this.username)
            data.append("password_1", this.password_1)
            data.append("password_2", this.password_2)
            axios.post('/api/publish/register', data)
                .then(response => {
                    switch (response.data.errno) {
                        case 0:
                            alert("注册成功")
                            break;
                        case 1001:
                            alert("请求方式错误")
                            break;
                        case 1002:
                            alert("用户名重复")
                            break;
                        case 1003:
                            alert("两次输入的密码不同")
                            break;
                        default:
                            break;
                    }
                })
        }
    }
}
</script>
