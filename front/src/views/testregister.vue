<template>
    <div>1</div>
    <el-button @click="send">send</el-button>
</template>
<script>
import axios from 'axios';
import Swal from 'sweetalert2';
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
            let data = new FormData();
            data.append("username", this.username)
            data.append("password_1", this.password_1)
            data.append("password_2", this.password_2)
            axios.post('/api/user/register', data).then(response => {
                if (response.data.errno === 0) {
                    Swal.fire("1")
                }
            })
        }
    }

}
</script>