import React, { useState, useEffect } from 'react';
import { View, StyleSheet, FlatList, Text, BackHandler } from 'react-native';
import SearchModal from '../components/SearchModal';
import setting from '../../secret.json';
import CardComponentForSubs from '../components/CardForSubs';
import { CategoryLabel } from '../functions/functions';
import ButtonModalForSubs from '../components/ButtonModalForSubs';
import ScreenHeaderForMain from '../components/ScreenHeaderForMain';
import Toast from 'react-native-root-toast';
import ButtonModal from '../components/ButtonModal';
import ScreenHeader from '../components/ScreenHeader';

const Subscribe = (props) => {
  const [visible1, setVisible1] = useState(false);
  const [visible2, setVisible2] = useState(false);
  const [current, setCurrent] = useState('All');
  const [text, setText] = useState('');
  const [tempText, setTempText] = useState('');
  const [fromFirst, setFromFirst] = useState(1);
  const [categoryLabel, setCategoryLabel] = useState('모두');
  const [reset, setReset] = useState(0);
  const [emotion, setEmotion] = useState('All');
  const [search, setSearch] = useState(0);

  useEffect(() => {
    const backAction = () => {
      setCurrent('All');
      setText('');
      setTempText('');
      if (fromFirst === 1) {
        setFromFirst(0);
      } else {
        setFromFirst(1);
      }
      props.navigation.navigate('Main');
      return true;
    };

    const backHandler = BackHandler.addEventListener(
      'hardwareBackPress',
      backAction
    );

    return () => backHandler.remove();
  }, []);

  useEffect(() => {
    Toast.show('구독한 언론사가 보이지 않으면 새로고침을 해주세요.', {
      duration: Toast.durations.LONG,
    });
  }, []);

  useEffect(() => {
    CategoryLabel(current, setCategoryLabel);
  }, [current]);
  return (
    <View style={styles.container}>
      <ButtonModal
        FsetVisible={setVisible1}
        FsetCurrent={setCurrent}
        setEmotion={setEmotion}
        emotion={emotion}
        search={search}
        setSearch={setSearch}
        currentValue={current}
        visibleValue={visible1}
        isMainOrSubs={true}
      />
      <SearchModal
        visibleValue={visible2}
        FsetVisible={setVisible2}
        FsetTempText={setTempText}
        tempTextValue={tempText}
        FsetText={setText}
        FsetVisible={setVisible2}
        FsetReset={setReset}
        reset={reset}
      />
      <ScreenHeader
        screenName="구독"
        FsetVisible1={setVisible1}
        FsetVisible2={setVisible2}
        categoryLabelValue={categoryLabel}
        navigation={props.navigation}
        FsetReset={setReset}
        reset={reset}
      />
      <CardComponentForSubs
        pressURL={setting['URL'] + 'read_subs/'}
        search={text}
        category={current}
        emotion={emotion}
        fromFirst={fromFirst}
        search2={search}
        reset={reset}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
export default Subscribe;
