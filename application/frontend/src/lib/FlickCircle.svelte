<script>
    export let inputCharacters;
</script>

<div class="flick_circle">
    <div class="sub_circle blank_circle"></div>
    <div class="sub_circle"><p class="sub_char">{inputCharacters.up}</p></div>
    <div class="sub_circle blank_circle"></div>

    <div class="sub_circle"> <p class="sub_char">{inputCharacters.left}</p> </div>
    <div class="core_circle">
      <p class="core_char">{inputCharacters.core}</p>
    </div>
    <div class="sub_circle"><p class="sub_char">{inputCharacters.right}</p></div>

    <div class="sub_circle blank_circle"></div>
    <div class="sub_circle"><p class="sub_char">{inputCharacters.down}</p></div>
    <div class="sub_circle blank_circle"></div>

  </div>

<style>
  .flick_circle {
    width: var(--flick-radius);
    height: var(--flick-radius);
    border-radius: var(--flick-radius);
    background-color: pink;
    display: grid;
    grid-template-rows: 2fr 3fr 2fr;
    grid-template-columns: 2fr 3fr 2fr;
  }
  .core_circle, .sub_circle {
    align-self: center;
    justify-self: center;
  }
  .core_circle {
    width: var(--core-radius);
    height: var(--core-radius);
    border-radius: var(--core-radius);
    background-color: cyan;
  }
  .core_circle, .sub_circle {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .core_char {
    font-size: var(--core-radius);
    font-weight: 500;
  }
  .sub_char {
    font-size: var(--sub-radius);
  }
  .sub_circle, .blank_circle {
    width: var(--sub-radius);
    height: var(--sub-radius);
    border-radius: var(--sub-radius);
    background-color: lightyellow;
  }
  .blank_circle {
    background-color: transparent;
  }
</style>