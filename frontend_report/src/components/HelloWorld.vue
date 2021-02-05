<template>
  <div class="hello">
    <h1>API Report</h1>
    <div>
      IBM on the NYSE (Internal): {{ibm_v}}
    </div>
    <div>
      Temperature in Warrington (External): {{temp_f}}
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      ibm_v: 0,
      WEATHER_KEY: "",
      temp_f: 0
    }
  },
  async mounted() {
    await axios({ method: "GET", "url": "http://localhost/ibm" })
          .then(result => {
            this.ibm_v = result.data['ibm_v'];
          }, (err) => {
            console.error(err);
          });

    await axios({ method: "GET", "url": "http://localhost/weather" })
          .then(result => {
            this.temp_f = result.data['temp_f'];
          }, (err) => {
            console.error(err);
          });
  }
}
</script>

<!-- Leave default CSS -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
