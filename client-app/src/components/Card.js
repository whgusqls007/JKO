import React, { useState, useEffect, useRef } from 'react';
import {
  Text,
  View,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  Image,
} from 'react-native';
import {
  loadData,
  loadExtraData,
  toTop,
  setFalse,
  setTrue,
} from '../functions/functions';
import ArticleModal from './ArticleModal';

const CardComponent = (props) => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [prevText, setPrevText] = useState('');
  const [prevCategory, setPrevCategory] = useState('All');
  const [firstParam, setFirstParam] = useState(10);
  const [secondParam, setSecondParam] = useState(19);
  const [fromFirst, setFromFirst] = useState(1);
  const [reset, setReset] = useState(1);
  const flatListRef = useRef();

  if (fromFirst !== props.fromFirst) {
    setFromFirst(props.fromFirst);
  }

  if (prevText !== props.search) {
    setPrevText(props.search);
  }

  if (prevCategory !== props.category) {
    setPrevCategory(props.category);
  }

  if (reset !== props.reset) {
    setReset(props.reset);
  }

  useEffect(() => {
    loadData(
      props.pressURL,
      props.search,
      props.category,
      setData,
      setLoading,
      props.emotion
    );
    setFirstParam(10);
    setSecondParam(19);
  }, []);

  useEffect(() => {
    setData([]);
    setLoading(true);
    loadData(
      props.pressURL,
      props.search,
      props.category,
      setData,
      setLoading,
      props.emotion
    );
    setFirstParam(10);
    setSecondParam(19);
    toTop(flatListRef);
  }, [prevText, reset, props.search2]);

  useEffect(() => {
    toTop(flatListRef);
  }, [fromFirst]);

  const Item = ({ item }) => {
    return (
      <View>
        <ArticleModal
          item={item}
          FsetFalse={setFalse}
          data={data}
          FsetData={setData}
        />

        <TouchableOpacity
          onPress={() => setTrue(item.id, data, setData)}
          style={{
            alignContent: 'center',
            alignItems: 'center',
          }}
        >
          <View style={styles.cardLayout}>
            {item.img !== '' ? (
              <Image source={{ uri: item.img }} style={styles.imageArea} />
            ) : null}
            <View style={styles.textArea}>
              <Text style={{ fontSize: 20, fontWeight: 'bold' }}>
                {item.title}
              </Text>
              {!Array.isArray(item.url) ? (
                <>
                  <Text style={{ fontWeight: 'bold' }}>{item.press}</Text>
                  <Text style={{ fontWeight: 'bold' }}>
                    감정 : {item.emotion}
                  </Text>
                </>
              ) : (
                <>
                  <Text style={{ fontWeight: 'bold' }}>
                    {item.press.map((d) => {
                      return d + '   ';
                    })}
                  </Text>
                  <Text style={{ fontWeight: 'bold' }}>
                    감정 : {item.emotion}
                  </Text>
                </>
              )}
              <Text></Text>
              <Text numberOfLines={3}>{item.mainText}</Text>
            </View>
          </View>
        </TouchableOpacity>
      </View>
    );
  };
  return (
    <View style={styles.container}>
      <FlatList
        style={{ width: '100%' }}
        data={data}
        renderItem={(item) => {
          return Item(item);
        }}
        onRefresh={() => {
          setData([]);
          loadData(
            props.pressURL,
            props.search,
            props.category,
            setData,
            setLoading,
            props.emotion
          );
          setFirstParam(10);
          setSecondParam(19);
        }}
        refreshing={loading}
        keyExtractor={(item) => item.id}
        onEndReached={() => {
          setLoading(true);
          loadExtraData(
            setData,
            setFirstParam,
            setSecondParam,
            setLoading,
            firstParam,
            secondParam,
            prevText,
            prevCategory,
            props.pressURL,
            props.emotion,
            data
          );
        }}
        onEndReachedThreshold={0.9}
        ref={flatListRef}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignContent: 'center',
    alignItems: 'center',
    width: '100%',
  },
  cardLayout: {
    flexDirection: 'row',
    width: '95%',
    borderWidth: 1,
    marginTop: '1%',
    marginBottom: '1%',
    backgroundColor: 'white',
    alignContent: 'center',
    alignItems: 'center',
  },
  imageArea: {
    width: '35%',
    height: '90%',
    margin: '2%',
    resizeMode: 'stretch',
  },
  textArea: {
    flex: 1,
    flexDirection: 'column',
    margin: '2%',
  },
});

export default CardComponent;
