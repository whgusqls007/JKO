import React from 'react';
import { Modal } from 'react-native';
import ButtonModalDetail from '../components/ButtonModalDetail';
import Constants from 'expo-constants';

const ButtonModal = (props) => {
  return (
    <Modal
      animationType="fade"
      transparent={true}
      visible={props.visibleValue}
      onRequestClose={() => props.FsetVisible(false)}
      style={{ opacity: 0.1 }}
    >
      <ButtonModalDetail
        FsetVisible={props.FsetVisible}
        FsetCurrent={props.FsetCurrent}
        currentValue={props.currentValue}
        name={props.name}
        pressName={props.pressName}
        emotion={props.emotion}
        setEmotion={props.setEmotion}
        search={props.search}
        setSearch={props.setSearch}
        isMainOrSubs={props.isMainOrSubs}
        isMain={props.isMain}
        cluster={props.cluster}
        setCluster={props.setCluster}
      />
    </Modal>
  );
};
export default ButtonModal;
