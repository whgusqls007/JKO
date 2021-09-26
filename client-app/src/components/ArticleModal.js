import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  Modal,
  ScrollView,
  Linking,
  Image,
} from 'react-native';
import Constants from 'expo-constants';
import { AntDesign } from '@expo/vector-icons';

const ArticleModal = (props) => {
  return (
    <Modal
      animationType="slide"
      transparent={false}
      visible={props.item.visible}
      onRequestClose={() =>
        props.FsetFalse(props.item.id, props.data, props.FsetData)
      }
    >
      <AntDesign.Button
        name="back"
        size={24}
        color="black"
        backgroundColor="white"
        onPress={() => {
          props.FsetFalse(props.item.id, props.data, props.FsetData);
        }}
        style={{ paddingLeft: 20, marginTop: Constants.statusBarHeight }}
      >
        <Text>뒤로 가기</Text>
      </AntDesign.Button>
      <ScrollView>
        <View style={styles.container}>
          <Text style={styles.titleSize}>{props.item.title}</Text>
          <Text />
          {!Array.isArray(props.item.url) ? (
            <>
              <Text style={styles.titleSubElement}>{props.item.press}</Text>
              <Text style={{ fontWeight: 'bold' }}>
                감정 : {props.item.emotion}
              </Text>
            </>
          ) : (
            <>
              <Text style={styles.titleSubElement}>
                {props.item.press.map((d) => {
                  return d + '   ';
                })}
              </Text>
              <Text style={styles.titleSubElement}>
                감정 : {props.item.emotion}
              </Text>
            </>
          )}
          <Text style={styles.titleSubElement}>{props.item.date}</Text>
          <Text style={styles.titleSubElement}>{props.item.reporter}</Text>
        </View>
        <View style={styles.container}>
          {props.item.img !== '' ? (
            <Image
              source={{ uri: props.item.img }}
              style={{
                width: '100%',
                height: 300,
                marginBottom: 50,
                resizeMode: 'stretch',
              }}
            />
          ) : null}
          <Text style={styles.articleSize}>{props.item.mainText}</Text>
          <Text />
          {!Array.isArray(props.item.url) ? (
            <Text
              style={styles.hyperlinkSize}
              onPress={() => {
                Linking.openURL(props.item.url);
              }}
            >
              본문 보러가기 (클릭)
            </Text>
          ) : (
            props.item.url.map((url, index) => {
              return (
                <Text
                  key={index}
                  style={styles.hyperlinkSize}
                  onPress={() => {
                    Linking.openURL(url);
                  }}
                >
                  {props.item.press[index]} 보러가기 (클릭)
                </Text>
              );
            })
          )}
        </View>
      </ScrollView>
    </Modal>
  );
};

const styles = StyleSheet.create({
  container: {
    margin: 10,
    marginBottom: 5,
    marginTop: 5,
    backgroundColor: 'white',
    borderColor: 'black',
    borderWidth: 1,
    padding: 35,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
    textAlign: 'left',
  },
  titleSize: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  titleSubElement: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  articleSize: {
    fontSize: 16,
  },
  hyperlinkSize: {
    fontSize: 20,
  },
});

export default ArticleModal;
