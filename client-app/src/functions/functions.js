import AsyncStorage from '@react-native-async-storage/async-storage';

export const getItemFromAsync = (storageName) => {
  if (isEmpty(storageName)) {
    throw Error('Storage Name is empty');
  }

  return new Promise((resolve, reject) => {
    AsyncStorage.getItem(storageName, (err, result) => {
      if (err) {
        reject(err);
      }

      if (result === null) {
        resolve(null);
      }

      resolve(JSON.parse(result));
    });
  });
};

export const setItemToAsync = (storageName, item) => {
  if (isEmpty(storageName)) {
    throw Error('Storage Name is empty');
  }

  return new Promise((resolve, reject) => {
    AsyncStorage.setItem(storageName, JSON.stringify(item), (error) => {
      if (error) {
        reject(error);
      }

      resolve('입력 성공');
    });
  });
};

export const isEmpty = function (value) {
  if (
    value === '' ||
    value === null ||
    value === undefined ||
    (value !== null && typeof value === 'object' && !Object.keys(value).length)
  ) {
    return true;
  } else {
    return false;
  }
};

export const setFalse = (ID, data, setData) => {
  setData(
    data.map((item) => {
      if (item.id === ID) {
        return {
          id: item.id,
          title: item.title,
          mainText: item.mainText,
          reporter: item.reporter,
          date: item.date,
          url: item.url,
          press: item.press,
          mainPress: item.mainPress,
          img: item.img,
          emotion: item.emotion,
          visible: false,
        };
      } else {
        return item;
      }
    })
  );
};

export const setTrue = (ID, data, setData) => {
  setData(
    data.map((item) => {
      if (item.id === ID) {
        return {
          id: item.id,
          title: item.title,
          mainText: item.mainText,
          reporter: item.reporter,
          date: item.date,
          url: item.url,
          press: item.press,
          mainPress: item.mainPress,
          img: item.img,
          emotion: item.emotion,
          visible: true,
        };
      } else {
        return item;
      }
    })
  );
};

const list = [
  'read_busan/',
  'read_donga/',
  'read_hangook/',
  'read_herald/',
  'read_joongang/',
  'read_joseon/',
  'read_nocut/',
  'read_ohmynews/',
  'read_wikitree/',
  'read_yeonhap/',
];

export const getUrl = () => {
  return new Promise((resolve, reject) => {
    var urls = [];
    for (let i = 0; i < 10; i++) {
      getItemFromAsync(list[i]).then((url) => {
        if (url !== null && url.saved !== false) {
          urls.push(url.saved);
        }
        if (i === 9) {
          resolve(urls);
        }
      });
    }
  });
};

export const loadData = (
  URL,
  search,
  category,
  setData,
  setLoading,
  emotion
) => {
  fetch(URL, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      first: 0,
      last: 9,
      text: search,
      category: category,
      emotion: emotion,
    }),
  })
    .then((response) => response.json())
    .then((loadedData) => {
      setData(loadedData);
      setLoading(false);
    })
    .catch((e) => console.log(e));
};

export const loadExtraData = (
  setData,
  setFirstParam,
  setSecondParam,
  setLoading,
  firstParam,
  secondParam,
  prevText,
  prevCategory,
  URL,
  emotion,
  data
) => {
  fetch(URL, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      first: firstParam,
      last: secondParam,
      text: prevText,
      category: prevCategory,
      emotion: emotion,
    }),
  })
    .then((response) => response.json())
    .then((loadedData) => {
      console.log(loadedData);
      setData([...data, ...loadedData]);
      setFirstParam(secondParam + 1);
      setSecondParam(secondParam + 10);
      setLoading(false);
    })
    .catch((e) => console.log(e));
};

export const toTop = (flatListRef) => {
  flatListRef.current.scrollToOffset({ animated: true, index: -1 });
};

export const loadDataForSubs = (
  URL,
  search,
  category,
  setData,
  setLoading,
  urls,
  emotion
) => {
  fetch(URL, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      first: 0,
      last: 4,
      text: search,
      category: category,
      classNames: urls,
      emotion: emotion,
    }),
  })
    .then((response) => response.json())
    .then((loadedData) => {
      setData(loadedData);
      setLoading(false);
    })
    .catch((e) => console.log(e));
};

export const loadExtraDataForSubs = (
  setData,
  setFirstParam,
  setSecondParam,
  setLoading,
  firstParam,
  secondParam,
  prevText,
  prevCategory,
  URL,
  data,
  urls,
  emotion
) => {
  fetch(URL, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      first: firstParam,
      last: secondParam,
      text: prevText,
      category: prevCategory,
      classNames: urls,
      emotion: emotion,
    }),
  })
    .then((response) => response.json())
    .then((loadedData) => {
      setData([...data, ...loadedData]);
      setFirstParam(secondParam + 1);
      setSecondParam(secondParam + 5);
      setLoading(false);
    })
    .catch((e) => console.log(e));
};

export const CategoryLabel = (current, setCategoryLabel) => {
  if (current === 'All') {
    setCategoryLabel('모두');
  } else if (current === 'sport') {
    setCategoryLabel('스포츠');
  } else if (current === 'politics') {
    setCategoryLabel('정치');
  } else if (current === 'society') {
    setCategoryLabel('사회');
  } else {
    setCategoryLabel('경제');
  }
  return;
};
