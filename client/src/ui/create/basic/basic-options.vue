<template>
  <div class="basic-outer">
    <h1 class="section-head">{{number}}. Balance Users</h1>
    <h6 class="section-desc">Modify the relative influence of each user's taste on the final product.</h6>
    <div class="row"
      v-for="user in group">
      <div class="col col-md-2">
        {{user}}
      </div>
      <div class="col col-md-10">
        <slider
          :min="1"
          :max="100"
          :textbox="false"
          :data="{'user': user}"
          v-on:value-change-data="updateValue"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Slider from '@/components/slider/slider';

export default {
  name: 'basic-options',
  data () {
    return {
      group: [],
      balance: {},
    };
  },
  props: {
    number: Number,
  },
  methods: {
    updateGroup(newGroup) {
      this.group = newGroup;
      this.emitOptions();
    },
    updateValue(data) {
      this.balance[data["data"]["user"]] = String(data["value"]);
      this.emitOptions();
    },
    emitOptions() {
      var pass = {};
      for (var ix=0; ix<this.group.length; ix++){
        let user = this.group[ix];
        pass[user] = this.balance[user];
      }
      this.$eventHub.$emit("create-current-basic-options", pass);
    }
  },
  components: {
    'slider': Slider,
  },
  created() {
    this.$eventHub.$on("create-current-group", this.updateGroup);
  },
  beforeDestroy() {
    this.$eventHub.$off("create-current-group");
  },
};
</script>

<style>
.basic-outer {

}

.card-header {
  cursor: pointer;
}

.form-group {
  padding-bottom: 10px;
}
</style>
