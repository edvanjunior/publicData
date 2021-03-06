import React from 'react';
import { FaCompress, FaExpand } from 'react-icons/fa';
import Button from '../../../../Common/Button';

interface Props extends React.ComponentProps<React.FC> {
  isExpanded: boolean;
}

const ExpanderButton: React.FC<Props> = ({ isExpanded }) => (
  <Button
    color="white"
    size="xs"
    title={isExpanded ? 'Collapse row' : 'Expand row'}
    // This is needed to remove focus on button when clicked (to avoid button style change)
    onMouseDown={e => {
      e.preventDefault();
    }}
    data-test={isExpanded ? 'collapse-event' : 'expand-event'}
  >
    {isExpanded ? <FaCompress /> : <FaExpand />}
  </Button>
);

export default ExpanderButton;
