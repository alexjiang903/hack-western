<template>
    <div>
        <h1>Home page</h1>
        <p> This is the home page of the website. </p>


        <p> two windows (transcription and definitions) go here</p>
    </div>


</template>


<script>
    //Script
    export default {
        name: 'Transcript',
        data() {
            return {
                message: 'Hello Vue!',
                text: ''
                
            }       
        },

        mounted() {
            console.log('Component mounted.')
        },

        methods() {
            // all methods 
            // get the text to display on screen, pass it to backend
            
            // Try to incorporate whisper-asr-demo as a method 
            
        }
        
        

    }




</script>