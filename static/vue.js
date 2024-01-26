import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

createApp({
  delimiters: ['{$', '$}'],
  setup() 
  {
    return 
    {
      count: ref(0)
    }
  }
}).mount('#app')