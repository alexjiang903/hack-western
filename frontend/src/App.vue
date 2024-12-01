<script setup>
import { ref, computed } from 'vue'
import Translation from './components/Translations.vue'
import Transcript from './Transcript.vue'
// import NotFound from './components/NotFound.vue' (create error screen later)
import AudioRecord from './AudioRecord.vue'

// I got this from: https://vuejs.org/guide/scaling-up/routing#simple-routing-from-scratch
// Import *.vue components here, acts as root of application. (skeleton)

const routes = {
  '/': Translation,
  '/Transcript': Transcript,
  "/AudioRecord": AudioRecord
  
}


const currentPath = ref(window.location.hash.slice(1) || '/')

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash.slice(1) || '/'
})

const currentView = computed(() => {
  return routes[currentPath.value]
})
</script>

<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gray-50">
    <Transcript />
    <Translation/>
    <AudioRecord/>
  </div>
</template>

<style>
.inline-link {
  display: inline-block;
  margin-right: 10px;
}

</style>