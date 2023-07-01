<template>
    <div>
        <el-input v-model="password" placeholder="Please input"
            :suffix-icon="passwordValid ? 'el-icon-circle-check' : 'el-icon-circle-close'"
            @focus="showPasswordRequirements = true" @blur="showPasswordRequirements = false" />
        <el-popover v-model="showPasswordRequirements" placement="bottom" width="200px" trigger="manual">
            <p v-show="!passwordValid" style="color: red">密码至少8个字符，包括至少一个大写字母、一个小写字母和一个数字</p>
            <p v-show="passwordValid" style="color: green">密码要求满足</p>
        </el-popover>
    </div>
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
    <div style="font-size: 20px">
        <!-- 由于SVG图标默认不携带任何属性 -->
        <!-- 你需要直接提供它们 -->
        <Edit style="width: 1em; height: 1em; margin-right: 8px" />
        <Share style="width: 1em; height: 1em; margin-right: 8px" />
        <Delete style="width: 1em; height: 1em; margin-right: 8px" />
        <Search style="width: 1em; height: 1em; margin-right: 8px" />
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            password: '',
            showPasswordRequirements: false
        }
    },
    computed: {
        passwordValid() {
            // 检查密码是否符合要求的逻辑
            // 返回 true 或 false
            const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
            return passwordRegex.test(this.password);
        }
    }
}
</script>
  