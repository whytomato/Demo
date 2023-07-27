<template>
    <el-popover placement="bottom" title="Title" :width="400" trigger="click"
        content="this is content, this is content, this is content">
        <template #reference>
            <!-- <el-button class="m-2">Hover to activate</el-button> -->
            <el-input>123</el-input>
        </template>
    </el-popover>
    <el-popover v-model="showPasswordRequirements" placement="bottom" width="500px" trigger="click">
        <p v-show="!passwordValid" style="color: red">密码至少8个字符，包括至少一个大写字母、一个小写字母和一个数字</p>
        <p v-show="passwordValid" style="color: green">密码要求满足</p>
        <template #reference>
            <el-input v-model="password" placeholder="Please input"
                :suffix-icon="passwordValid ? 'CircleCheck' : 'CircleClose'" @focus="showPasswordRequirements = true"
                @blur="showPasswordRequirements = false" />
        </template>
    </el-popover>
    <el-button :disabled="countdown > 0" @click="startCountdown">{{ buttonText }}</el-button>
    <div class="box">
        <h2>css</h2>
    </div>
</template>
<style>
.box {
    position: relative;
    width: 180px;
    height: 250px;
    background: rgba(0, 0, 0, 8);
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

.box h2 {
    color: white;
    font-size: 4em;
    text-shadow: 2px 2px pink;
    z-index: 1;

}

.box::before {
    content: "";
    position: absolute;
    width: 120px;
    height: 120%;
    background: linear-gradient(#00ccff, #d500f9);
    animation: rotate 4s linear infinite;

}

@keyframes rotate {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}

.box::after {
    content: "";
    position: absolute;
    background: #0e1538;
    inset: 5px;
    border-radius: 20px;
}
</style>
<script>
export default {
    data() {
        return {
            password: '',
            showPasswordRequirements: false,
            countdown: 0,
            buttonText: '点击开始'
        }
    },
    computed: {
        passwordValid() {
            // 检查密码是否符合要求的逻辑
            // 返回 true 或 false
            const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
            return passwordRegex.test(this.password);
        }
    },
    methods: {
        startCountdown() {
            if (this.countdown === 0) {
                this.countdown = 10; // 设置倒计时时间为两分钟（120秒）
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
                this.buttonText = '点击开始';
            }
        },
    }
}
</script>
  