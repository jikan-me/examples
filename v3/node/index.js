import JikanNode from "jikan-node";

// an example of requesting a users entire list

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

const mal = new JikanNode();

async function requestAnimeList(username) {
  let animeEntries = [];
  let page = 1;
  while (true) {
    console.log(`Requesting ${username} ${page}`);
    const newResp = await mal.findUser(username, "animelist", "all", {
      page: page,
    });
    animeEntries.push(...newResp["anime"]);
    if (newResp["anime"].length < 300) {
      // returned less than 300 (typical amount in a pagination), exit
      break;
    }
    await sleep(3000);
    page += 1;
  }
  return animeEntries;
}

requestAnimeList("xinil").then((animeListData) => {
  animeListData.forEach((entry) => {
    console.log(entry.title);
  });
  console.log("Highest rated entry:");
  console.log(animeListData.sort((a, b) => a.score > b.score)[0]);
  console.log(`Finished requesting ${animeListData.length} entries`);
});
