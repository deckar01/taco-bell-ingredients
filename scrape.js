// https://www.tacobell.com/nutrition/info

const parser = new DOMParser();
async function load(id) {
    const url = `https://www.nutritionix.com/taco-bell/viewLabel/item/${id}/notFromAllergenPage`;
    const html = await fetch(url).then(r => r.text());
    const doc = parser.parseFromString(html, 'text/html');
    return Array.prototype.slice.call(doc.querySelectorAll('.weight strong'))
        .map(e => e.textContent);
}

const foods = Array.prototype.slice.call(document.querySelectorAll('.al'))
    .map(e => [
        e.childNodes[0].textContent,
        e.childNodes[0].id.split('-')[2]
    ]);

// NOTE: I stopped here and manually filtered the desired foods.

const ingredients = {};
(async () => {
    for([n, id] of foods) {
        ingredients[n] = await load(id);
    }
})().then(() => {
    console.log(JSON.stringify(ingredients));
});
