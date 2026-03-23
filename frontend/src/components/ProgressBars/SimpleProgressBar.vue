<template>
    <div class="simple-progress-bar">
        <div 
            class="progress" 
            :style="{ backgroundColor: progressBars[id - 1].status ? doneColor : defaultColor }"
            v-for="id in count" :key="id" :id="'progress-bar-'+id"
        ></div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';

const props = defineProps({
    count: {
        type: Number,
        default: 1
    },
    defaultColor: {
        type: String,
        default: "#000"
    },
    doneColor: {
        type: String,
        default: 'green'
    },
    progressBars: {
        type: Array,
        default: []
    }
});

for (let iter = 0; iter < props.count; iter++) {
    let newObj = {
        barNo: iter + 1,
        status: false,
    }
    
    props.progressBars.push(newObj)
}

const emits = defineEmits([
    'passInitValues'
])

onMounted(() => {
    emits('passInitValues', props.progressBars);
});

function updateProgressBar() {
    // if ()
}
</script>

<style scoped>
.simple-progress-bar {
    display: flex;
    align-items: center;
    gap: 3px;
}

.progress {
    flex-grow: 1;
    
    border-radius: 3px;
    height: 5px;
    transition: 0.3s;
}
</style>