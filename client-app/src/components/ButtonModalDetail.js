import React, { useState, useEffect } from 'react';
import { View, StyleSheet, Text } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { Checkbox } from 'react-native-paper';
import RadioButton from 'expo-radio-button';
import Constants from 'expo-constants';
import { getItemFromAsync, setItemToAsync } from '../functions/functions';
import EmotionRadio from './EmotionRadio';

const ButtonModalDetail = (props) => {
  const [isSelected, setSelection] = useState(false);
  const [category, setCategory] = useState('All');
  const [emotion, setEmotion] = useState('All');
  useEffect(() => {
    props.setEmotion('All');
  }, [category]);

  useEffect(() => {
    if (props.isMainOrSubs !== true) {
      getItemFromAsync(props.name).then((data) => {
        if (data !== null) {
          if (data.saved === props.name) {
            setSelection(true);
          } else if (data.saved === true) {
            setSelection(false);
            setItemToAsync(props.name, { saved: false });
          } else {
            setSelection(false);
          }
        } else {
          setSelection(false);
          setItemToAsync(props.name, { saved: false });
        }
      });
    }
  }, []);

  useEffect(() => {
    if (props.isMainOrSubs !== true) {
      getItemFromAsync(props.name).then((data) => {
        if (data !== null) {
          if (data.saved === props.name && isSelected === false) {
            setItemToAsync(props.name, { saved: false });
          } else if (data.saved === false && isSelected === true) {
            setItemToAsync(props.name, { saved: props.name });
          } else if (data.saved === false && isSelected === false) {
            setItemToAsync(props.name, { saved: false }).then(() => {});
          } else if (data.saved === props.name && isSelected === true) {
            setItemToAsync(props.name, { saved: props.name }).then(() => {});
          }
        } else {
          setItemToAsync(props.name, { saved: false });
        }
      });
    }
  }, [isSelected]);

  return (
    <View
      style={{
        backgroundColor: 'white',
        paddingTop: Constants.statusBarHeight,
      }}
    >
      <View style={{ flexWrap: 'nowrap' }}>
        <Text style={styles.textstyle}>카테고리</Text>
        <View style={styles.radioButtonView}>
          <RadioButton
            value="politics"
            selected={category}
            onSelected={(value) => {
              setCategory(value);
            }}
            radioBackground="blue"
          >
            <Text>정치</Text>
          </RadioButton>
          <RadioButton
            value="economy"
            selected={category}
            onSelected={(value) => {
              setCategory(value);
            }}
            radioBackground="blue"
          >
            <Text>경제</Text>
          </RadioButton>
          <RadioButton
            value="society"
            selected={category}
            onSelected={(value) => {
              setCategory(value);
            }}
            radioBackground="blue"
          >
            <Text>사회</Text>
          </RadioButton>
          <RadioButton
            value="sport"
            selected={category}
            onSelected={(value) => {
              setCategory(value);
            }}
            radioBackground="blue"
          >
            <Text>스포츠</Text>
          </RadioButton>
          <RadioButton
            value="All"
            selected={category}
            onSelected={(value) => {
              setCategory(value);
            }}
            radioBackground="blue"
          >
            <Text>모두</Text>
          </RadioButton>
        </View>
      </View>
      <EmotionRadio
        setEmotion={setEmotion}
        emotion={emotion}
        category={category}
      />
      <Text></Text>
      <View style={styles.closecircleView}>
        {props.isMainOrSubs === false ? (
          <View style={styles.subScribe}>
            <Checkbox
              status={isSelected ? 'checked' : 'unchecked'}
              onPress={() => {
                setSelection(!isSelected);
              }}
            />
            <Text style={styles.subScribeText}>구독</Text>
          </View>
        ) : null}
        {props.isMain === true ? (
          <View style={styles.subScribe}>
            <Checkbox
              status={props.cluster ? 'checked' : 'unchecked'}
              onPress={() => {
                props.setCluster(!props.cluster);
              }}
            />
            <Text style={styles.subScribeText}>중복 제거</Text>
          </View>
        ) : null}
        <AntDesign.Button
          name="search1"
          size={24}
          color="black"
          style={{ backgroundColor: 'white' }}
          onPress={() => {
            props.FsetCurrent(category);
            props.setEmotion(emotion);
            props.setSearch(!props.search);
            props.FsetVisible(false);
          }}
        >
          <Text>검색</Text>
        </AntDesign.Button>
        <AntDesign.Button
          name="closecircle"
          size={24}
          color="black"
          style={{
            backgroundColor: 'white',
            width: '120%',
          }}
          onPress={() => props.FsetVisible(false)}
        >
          <Text>닫기</Text>
        </AntDesign.Button>
      </View>
    </View>
  );
};
const styles = StyleSheet.create({
  closecircleView: {
    marginLeft: 'auto',
    flexDirection: 'row',
    marginTop: '2%',
    marginRight: '2%',
    textAlignVertical: 'center',
    alignContent: 'center',
    justifyContent: 'center',
  },
  radioButtonView: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingLeft: 30,
    paddingRight: 30,
    paddingTop: 20,
  },
  textstyle: {
    paddingLeft: 30,
    paddingTop: 30,
    fontSize: 20,
  },
  subScribe: {
    flexDirection: 'row',
  },
  subScribeText: {
    marginLeft: '5%',
    textAlign: 'center',
    textAlignVertical: 'center',
    marginRight: 0,
    marginTop: 'auto',
    marginBottom: 'auto',
    paddingRight: 0,
  },
  subScribeBox: {
    margin: 0,
    marginTop: 'auto',
    marginBottom: 'auto',
    padding: 0,
  },
});

export default ButtonModalDetail;
