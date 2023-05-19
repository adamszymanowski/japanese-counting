<script>
    import FlickCircle from './FlickCircle.svelte';
    import Key from './Key.svelte';
    
    const createInputCharacters = (characterArray) => {
        return { 
                                     up:   characterArray[2], 
            left: characterArray[1], core: characterArray[0], right: characterArray[3], 
                                     down: characterArray[4] 
        };
    }

    const aSet = createInputCharacters(["あ", "い", "う", "え", "お"]);
    const kaSet = createInputCharacters(["か", "き", "く", "け", "こ"]);
    const saSet = createInputCharacters(['さ', 'し', 'す', 'せ', 'そ']);
    const taSet = createInputCharacters(['た', 'ち', 'つ', 'て', 'と']);
    const naSet = createInputCharacters(['な', 'に', 'ぬ', 'ね', 'の']);
    const haSet = createInputCharacters(['は', 'ひ', 'ふ', 'へ', 'ほ']);
    const maSet = createInputCharacters(['ま', 'み', 'む', 'め', 'も']);
    const yaSet = createInputCharacters(['や', ' ', 'ゆ', ' ', 'よ']);
    const raSet = createInputCharacters(['ら', 'り', 'る', 'れ', 'ろ']);
    const characterSets = [aSet, kaSet, saSet, taSet, naSet, haSet, maSet, yaSet, raSet];
  </script>
  
<div class="keyboard">

    {#each characterSets as characters}
        <div>
            <FlickCircle inputCharacters={characters} />
        </div>
    {/each}
       
</div>

<style>
    .keyboard {
        display: grid;
        grid-template-rows: 1fr 1fr 1fr 1fr;
        grid-template-columns: 1fr 1fr 1fr;
    }
</style>
<!--
  <div class="keyboard">
    {#each ['あ', 'か', 'さ'] as char}
        <FlickCircle char={char} />
      <Key char={char} on:select={handleSelect} selected={selectedKey === char} />
    {/each}
  </div>
  
  <p>Input: {inputText}</p>
--> 