import React, { useState, useEffect } from 'react';
import { View, StyleSheet, Text } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { Checkbox } from 'react-native-paper';
import RadioButton from 'expo-radio-button';
import Constants from 'expo-constants';
import { getItemFromAsync, setItemToAsync } from '../functions/functions';

const EmotionRadio = (props) => {
  return (
    <>
      {props.category === 'politics' ? (
        <>
          <Text style={styles.textstyle}>감정</Text>
          <View style={styles.radioButtonView}>
            <RadioButton
              value="All"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>모두</Text>
            </RadioButton>
            <RadioButton
              value="positive"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>긍정</Text>
            </RadioButton>
            <RadioButton
              value="negative"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>부정</Text>
            </RadioButton>
          </View>
        </>
      ) : null}
      {props.category === 'economy' ? (
        <>
          <Text style={styles.textstyle}>감정</Text>
          <View style={styles.radioButtonView}>
            <RadioButton
              value="All"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>모두</Text>
            </RadioButton>
            <RadioButton
              value="positive"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>긍정</Text>
            </RadioButton>
            <RadioButton
              value="negative"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>부정</Text>
            </RadioButton>
            <RadioButton
              value="neutral"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>중립</Text>
            </RadioButton>
          </View>
        </>
      ) : null}
      {props.category === 'society' ? (
        <>
          <Text style={styles.textstyle}>감정</Text>
          <View style={styles.radioButtonView}>
            <RadioButton
              value="All"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>모두</Text>
            </RadioButton>
            <RadioButton
              value="warm"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>따뜻한</Text>
            </RadioButton>
            <RadioButton
              value="interesting"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>신기한</Text>
            </RadioButton>
          </View>
          <View style={styles.radioButtonView}>
            <RadioButton
              value="sad"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>슬픈</Text>
            </RadioButton>
            <RadioButton
              value="shocking"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>충격적</Text>
            </RadioButton>
            <RadioButton
              value="neutral"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>중립</Text>
            </RadioButton>
          </View>
        </>
      ) : null}
      {props.category === 'sport' ? (
        <>
          <Text style={styles.textstyle}>감정</Text>
          <View style={styles.radioButtonView}>
            <RadioButton
              value="All"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>모두</Text>
            </RadioButton>
            <RadioButton
              value="positive"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>긍정</Text>
            </RadioButton>
            <RadioButton
              value="negative"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>부정</Text>
            </RadioButton>
            <RadioButton
              value="neutral"
              selected={props.emotion}
              onSelected={(value) => {
                props.setEmotion(value);
              }}
              radioBackground="blue"
            >
              <Text>중립</Text>
            </RadioButton>
          </View>
        </>
      ) : null}
    </>
  );
};

const styles = StyleSheet.create({
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
});

export default EmotionRadio;
