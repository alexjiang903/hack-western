<script setup>
import { ref, computed } from 'vue'
import Translation from './components/Translations.vue'
import Transcript from './Transcript.vue'

// I got this from: https://vuejs.org/guide/scaling-up/routing#simple-routing-from-scratch
// Import *.vue components here, acts as root of application. (skeleton)

const routes = {
  '/': Translation,
  '/Transcript': Transcript
}


const currentPath = ref(window.location.hash.slice(1) || '/')

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash.slice(1) || '/'
})

const currentView = computed(() => {
  return routes[currentPath.value] || NotFound
})
</script>

<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gray-50">
    <component :is="currentView" />
  </div>
</template>

<style>
.inline-link {
  display: inline-block;
  margin-right: 10px;
}

</style>