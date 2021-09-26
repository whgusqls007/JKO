import React, { useState, useEffect } from 'react';
import { View, StyleSheet, Alert, BackHandler } from 'react-native';
import CardComponent from '../components/Card';
import SearchModal from '../components/SearchModal';
import ScreenHeaderForMain from '../components/ScreenHeaderForMain';
import setting from '../../secret.json';
import { CategoryLabel } from '../functions/functions';
import ButtonModalForSubs from '../components/ButtonModalForSubs';
import ButtonModal from '../components/ButtonModal';

const Main = (props) => {
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
        name="read_main/"
        pressName="메인"
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
      <ScreenHeaderForMain
        screenName="메인화면"
        FsetVisible1={setVisible1}
        FsetVisible2={setVisible2}
        categoryLabelValue={categoryLabel}
        navigation={props.navigation}
        FsetReset={setReset}
        reset={reset}
      />
      <CardComponent
        pressName="Main"
        pressURL={setting['URL'] + 'read_main/'}
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

export default Main;
