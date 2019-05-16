<template>
  <div>
    <div class="form-group row"
      v-if="textbox">
      <div class="col col-sm-3">
        <input style="width: 100%; height: 100%" type="number" class="form-control" v-model="value"/>
      </div>
      <div class="col col-sm-9">
        <b-form-input id="range-1" v-model="value" type="range" min="1" max="100"></b-form-input>
      </div>
    </div>
    <b-form-input id="range-1" v-model="value" type="range" min="1" max="100"
      v-else></b-form-input>
  </div>
</template>

<script>
export default {
  name: "slider",
  data() {
    return {
      value: 0,
    }
  },
  props: {
    min: Number,
    max: Number,
    textbox: Boolean,
    data: Object,
  },
  created() {
    this.value = Math.floor(this.min/2 + this.max/2);
  },
  watch: {
    value(newValue) {
      var data = {
        "data": this.data,
        "value": this.value,
      };
      this.$emit('value-change', newValue);
      this.$emit('value-change-data', data);
    }
  }
}
</script>

<style>
input[type=range] {
  -webkit-appearance: none;
}
input[type=range]:focus {
  outline: none;
}
input[type=range]::-webkit-slider-runnable-track {
  height: 8.4px;
  cursor: pointer;
  animate: 0.2s;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: #77438C;
  border-radius: 1.3px;
  border: 0.2px solid #010101;
}
input[type=range]::-webkit-slider-thumb {
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  border: 1px solid #000000;
  height: 36px;
  width: 16px;
  border-radius: 3px;
  background: #ffffff;
  cursor: pointer;
  -webkit-appearance: none;
  margin-top: -14px;
}
input[type=range]:focus::-webkit-slider-runnable-track {
  background: #77438C;
}
input[type=range]::-moz-range-track {
  width: 100%;
  height: 8.4px;
  cursor: pointer;
  animate: 0.2s;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: #77438C;
  border-radius: 1.3px;
  border: 0.2px solid #010101;
}
input[type=range]::-moz-range-thumb {
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  border: 1px solid #000000;
  height: 36px;
  width: 16px;
  border-radius: 3px;
  background: #ffffff;
  cursor: pointer;
}
input[type=range]::-ms-track {
  width: 100%;
  height: 8.4px;
  cursor: pointer;
  animate: 0.2s;
  background: transparent;
  border-color: transparent;
  border-width: 16px 0;
  color: transparent;
}
input[type=range]::-ms-fill-lower {
  background: #2a6495;
  border: 0.2px solid #010101;
  border-radius: 2.6px;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
}
input[type=range]::-ms-fill-upper {
  background: #77438C;
  border: 0.2px solid #010101;
  border-radius: 2.6px;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
}
input[type=range]::-ms-thumb {
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  border: 1px solid #000000;
  height: 36px;
  width: 16px;
  border-radius: 3px;
  background: #ffffff;
  cursor: pointer;
}
input[type=range]:focus::-ms-fill-lower {
  background: #77438C;
}
input[type=range]:focus::-ms-fill-upper {
  background: #367ebd;
}
</style>
