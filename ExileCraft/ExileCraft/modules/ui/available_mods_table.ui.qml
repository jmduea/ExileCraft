<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0" connectslotsbyname="false">
 <class>modpool_form_layout</class>
 <widget class="QWidget" name="modpool_form_layout">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>479</width>
    <height>362</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
  </property>
  <layout class="QFormLayout" name="formLayout">
   <property name="fieldGrowthPolicy">
    <enum>QFormLayout::ExpandingFieldsGrow</enum>
   </property>
   <property name="formAlignment">
    <set>Qt::AlignJustify|Qt::AlignVCenter</set>
   </property>
   <property name="horizontalSpacing">
    <number>0</number>
   </property>
   <property name="verticalSpacing">
    <number>0</number>
   </property>
   <property name="leftMargin">
    <number>0</number>
   </property>
   <property name="topMargin">
    <number>0</number>
   </property>
   <property name="rightMargin">
    <number>0</number>
   </property>
   <property name="bottomMargin">
    <number>0</number>
   </property>
   <item row="0" column="1">
    <widget class="QWidget" name="modpool_widget" native="true">
     <property name="sizePolicy">
      <sizepolicy hsizetype="MinimumExpanding" vsizetype="MinimumExpanding">
       <horstretch>0</horstretch>
       <verstretch>0</verstretch>
      </sizepolicy>
     </property>
     <property name="minimumSize">
      <size>
       <width>110</width>
       <height>200</height>
      </size>
     </property>
     <property name="maximumSize">
      <size>
       <width>360</width>
       <height>360</height>
      </size>
     </property>
     <layout class="QVBoxLayout" name="verticalLayout_2">
      <property name="spacing">
       <number>0</number>
      </property>
      <property name="leftMargin">
       <number>0</number>
      </property>
      <property name="topMargin">
       <number>0</number>
      </property>
      <property name="rightMargin">
       <number>0</number>
      </property>
      <property name="bottomMargin">
       <number>0</number>
      </property>
      <item>
       <widget class="QWidget" name="modpool_btns_layout" native="true">
        <layout class="QHBoxLayout" name="horizontalLayout">
         <property name="spacing">
          <number>0</number>
         </property>
         <property name="leftMargin">
          <number>0</number>
         </property>
         <property name="topMargin">
          <number>0</number>
         </property>
         <property name="rightMargin">
          <number>0</number>
         </property>
         <property name="bottomMargin">
          <number>0</number>
         </property>
         <item>
          <widget class="QPushButton" name="prefix_btn">
           <property name="text">
            <string>PushButton</string>
           </property>
           <property name="checkable">
            <bool>true</bool>
           </property>
           <property name="flat">
            <bool>false</bool>
           </property>
           <attribute name="buttonGroup">
            <string notr="true">modpool_btns</string>
           </attribute>
          </widget>
         </item>
         <item>
          <widget class="QPushButton" name="suffix_btn">
           <property name="text">
            <string>PushButton</string>
           </property>
           <property name="checkable">
            <bool>true</bool>
           </property>
           <property name="flat">
            <bool>false</bool>
           </property>
           <attribute name="buttonGroup">
            <string notr="true">modpool_btns</string>
           </attribute>
          </widget>
         </item>
         <item>
          <widget class="QPushButton" name="implicit_btn">
           <property name="styleSheet">
            <string notr="true">QPushButton {
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(109, 60, 60, 1), stop:1 rgba(136, 75, 75, 255));
margin: 0px;
font-family: Open Sans;
font-size: 14px;
font-weight: bold;
text-transform: uppercase;
box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba (0, 0, 0, 0.31);
border: 1px solid #000;
color: #FFF;
text-shadow: 1px 1px #000;
padding: 5px 10 px;
}</string>
           </property>
           <property name="text">
            <string>PushButton</string>
           </property>
           <property name="checkable">
            <bool>true</bool>
           </property>
           <property name="default">
            <bool>false</bool>
           </property>
           <property name="flat">
            <bool>false</bool>
           </property>
           <attribute name="buttonGroup">
            <string notr="true">modpool_btns</string>
           </attribute>
          </widget>
         </item>
        </layout>
       </widget>
      </item>
      <item>
       <widget class="QStackedWidget" name="modpool_container">
        <property name="sizePolicy">
         <sizepolicy hsizetype="MinimumExpanding" vsizetype="MinimumExpanding">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="frameShape">
         <enum>QFrame::NoFrame</enum>
        </property>
        <property name="frameShadow">
         <enum>QFrame::Plain</enum>
        </property>
        <widget class="QWidget" name="prefix_container" native="true">
         <layout class="QVBoxLayout" name="verticalLayout_32">
          <property name="spacing">
           <number>0</number>
          </property>
          <property name="leftMargin">
           <number>0</number>
          </property>
          <property name="topMargin">
           <number>0</number>
          </property>
          <property name="rightMargin">
           <number>0</number>
          </property>
          <property name="bottomMargin">
           <number>0</number>
          </property>
          <item>
           <widget class="CustomTreeView" name="prefix_tree_view">
            <property name="sizePolicy">
             <sizepolicy hsizetype="MinimumExpanding" vsizetype="MinimumExpanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="focusPolicy">
             <enum>Qt::TabFocus</enum>
            </property>
            <property name="frameShape">
             <enum>QFrame::StyledPanel</enum>
            </property>
            <property name="frameShadow">
             <enum>QFrame::Raised</enum>
            </property>
            <property name="verticalScrollBarPolicy">
             <enum>Qt::ScrollBarAlwaysOn</enum>
            </property>
            <property name="sizeAdjustPolicy">
             <enum>QAbstractScrollArea::AdjustToContentsOnFirstShow</enum>
            </property>
            <property name="alternatingRowColors">
             <bool>false</bool>
            </property>
            <property name="textElideMode">
             <enum>Qt::ElideRight</enum>
            </property>
            <property name="horizontalScrollMode">
             <enum>QAbstractItemView::ScrollPerItem</enum>
            </property>
            <property name="indentation">
             <number>10</number>
            </property>
            <property name="uniformRowHeights">
             <bool>true</bool>
            </property>
            <attribute name="headerCascadingSectionResizes">
             <bool>false</bool>
            </attribute>
            <attribute name="headerMinimumSectionSize">
             <number>80</number>
            </attribute>
            <attribute name="headerStretchLastSection">
             <bool>false</bool>
            </attribute>
           </widget>
          </item>
         </layout>
        </widget>
        <widget class="QWidget" name="suffix_container" native="true">
         <layout class="QVBoxLayout" name="verticalLayout_33">
          <property name="spacing">
           <number>0</number>
          </property>
          <property name="leftMargin">
           <number>0</number>
          </property>
          <property name="topMargin">
           <number>0</number>
          </property>
          <property name="rightMargin">
           <number>0</number>
          </property>
          <property name="bottomMargin">
           <number>0</number>
          </property>
          <item>
           <widget class="CustomTreeView" name="suffix_tree_view">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="frameShape">
             <enum>QFrame::StyledPanel</enum>
            </property>
            <property name="frameShadow">
             <enum>QFrame::Raised</enum>
            </property>
            <property name="verticalScrollBarPolicy">
             <enum>Qt::ScrollBarAlwaysOn</enum>
            </property>
            <property name="sizeAdjustPolicy">
             <enum>QAbstractScrollArea::AdjustToContentsOnFirstShow</enum>
            </property>
            <property name="alternatingRowColors">
             <bool>false</bool>
            </property>
            <property name="horizontalScrollMode">
             <enum>QAbstractItemView::ScrollPerItem</enum>
            </property>
            <property name="indentation">
             <number>10</number>
            </property>
            <property name="uniformRowHeights">
             <bool>true</bool>
            </property>
            <attribute name="headerCascadingSectionResizes">
             <bool>false</bool>
            </attribute>
            <attribute name="headerMinimumSectionSize">
             <number>80</number>
            </attribute>
            <attribute name="headerStretchLastSection">
             <bool>false</bool>
            </attribute>
           </widget>
          </item>
         </layout>
        </widget>
        <widget class="QWidget" name="implicit_container" native="true">
         <layout class="QVBoxLayout" name="verticalLayout_34">
          <property name="spacing">
           <number>0</number>
          </property>
          <property name="leftMargin">
           <number>0</number>
          </property>
          <property name="topMargin">
           <number>0</number>
          </property>
          <property name="rightMargin">
           <number>0</number>
          </property>
          <property name="bottomMargin">
           <number>0</number>
          </property>
          <item>
           <widget class="CustomTreeView" name="implicit_tree_view">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="frameShape">
             <enum>QFrame::StyledPanel</enum>
            </property>
            <property name="frameShadow">
             <enum>QFrame::Raised</enum>
            </property>
            <property name="verticalScrollBarPolicy">
             <enum>Qt::ScrollBarAlwaysOn</enum>
            </property>
            <property name="sizeAdjustPolicy">
             <enum>QAbstractScrollArea::AdjustToContentsOnFirstShow</enum>
            </property>
            <property name="alternatingRowColors">
             <bool>false</bool>
            </property>
            <property name="horizontalScrollMode">
             <enum>QAbstractItemView::ScrollPerItem</enum>
            </property>
            <property name="indentation">
             <number>10</number>
            </property>
            <property name="uniformRowHeights">
             <bool>true</bool>
            </property>
            <attribute name="headerCascadingSectionResizes">
             <bool>false</bool>
            </attribute>
            <attribute name="headerMinimumSectionSize">
             <number>80</number>
            </attribute>
            <attribute name="headerStretchLastSection">
             <bool>false</bool>
            </attribute>
           </widget>
          </item>
         </layout>
        </widget>
       </widget>
      </item>
     </layout>
    </widget>
   </item>
   <item row="0" column="0">
    <widget class="QWidget" name="history_widget" native="true">
     <property name="styleSheet">
      <string notr="true"/>
     </property>
     <layout class="QVBoxLayout" name="verticalLayout">
      <property name="spacing">
       <number>0</number>
      </property>
      <property name="leftMargin">
       <number>0</number>
      </property>
      <property name="topMargin">
       <number>0</number>
      </property>
      <property name="rightMargin">
       <number>0</number>
      </property>
      <property name="bottomMargin">
       <number>0</number>
      </property>
      <item>
       <widget class="QWidget" name="crafting_toolbox" native="true">
        <property name="sizePolicy">
         <sizepolicy hsizetype="MinimumExpanding" vsizetype="MinimumExpanding">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <property name="minimumSize">
         <size>
          <width>120</width>
          <height>0</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>200</width>
          <height>360</height>
         </size>
        </property>
        <property name="styleSheet">
         <string notr="true"/>
        </property>
        <layout class="QVBoxLayout" name="verticalLayout_37">
         <property name="spacing">
          <number>0</number>
         </property>
         <property name="leftMargin">
          <number>0</number>
         </property>
         <property name="topMargin">
          <number>0</number>
         </property>
         <property name="rightMargin">
          <number>0</number>
         </property>
         <property name="bottomMargin">
          <number>0</number>
         </property>
         <item>
          <widget class="QWidget" name="widget_2" native="true">
           <property name="styleSheet">
            <string notr="true"/>
           </property>
           <layout class="QVBoxLayout" name="verticalLayout_8">
            <property name="spacing">
             <number>0</number>
            </property>
            <property name="leftMargin">
             <number>0</number>
            </property>
            <property name="topMargin">
             <number>0</number>
            </property>
            <property name="rightMargin">
             <number>0</number>
            </property>
            <property name="bottomMargin">
             <number>0</number>
            </property>
            <item>
             <widget class="QToolBox" name="crafting_history">
              <property name="enabled">
               <bool>true</bool>
              </property>
              <property name="sizePolicy">
               <sizepolicy hsizetype="MinimumExpanding" vsizetype="MinimumExpanding">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>0</width>
                <height>0</height>
               </size>
              </property>
              <property name="font">
               <font>
                <family>Open Sans</family>
                <pointsize>-1</pointsize>
                <italic>false</italic>
                <bold>true</bold>
               </font>
              </property>
              <property name="styleSheet">
               <string notr="true">QWidget {
	vertical-align: top;
	padding: 5px 10px;
	text-shadow: 1px 1px #000;
	
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));

	border: 0px solid #000;
	box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0,.31);
	box-sizing: border-box;
	text-transform: uppercase;
	font-weight: bold;
	color: #f6e5b2;
	font-family: Open Sans;
	font-size: 14px;
	margin: 0px;
}</string>
              </property>
              <property name="frameShape">
               <enum>QFrame::StyledPanel</enum>
              </property>
              <property name="frameShadow">
               <enum>QFrame::Raised</enum>
              </property>
              <property name="currentIndex">
               <number>2</number>
              </property>
              <property name="tabSpacing">
               <number>0</number>
              </property>
              <widget class="QWidget" name="history_tab">
               <property name="geometry">
                <rect>
                 <x>0</x>
                 <y>0</y>
                 <width>80</width>
                 <height>168</height>
                </rect>
               </property>
               <property name="font">
                <font>
                 <family>Open Sans</family>
                 <pointsize>-1</pointsize>
                 <bold>true</bold>
                </font>
               </property>
               <property name="autoFillBackground">
                <bool>false</bool>
               </property>
               <property name="styleSheet">
                <string notr="true">QWidget {
	vertical-align: top;
	padding: 5px 10px;
	text-shadow: 1px 1px #000;
	
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));

	border: 0px solid #000;
	box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0,.31);
	box-sizing: border-box;
	text-transform: uppercase;
	font-weight: bold;
	color: #f6e5b2;
	font-family: Open Sans;
	font-size: 14px;
	margin: 0px;
}</string>
               </property>
               <attribute name="label">
                <string>History</string>
               </attribute>
               <layout class="QVBoxLayout" name="verticalLayout_20">
                <property name="spacing">
                 <number>0</number>
                </property>
                <property name="leftMargin">
                 <number>0</number>
                </property>
                <property name="topMargin">
                 <number>0</number>
                </property>
                <property name="rightMargin">
                 <number>0</number>
                </property>
                <property name="bottomMargin">
                 <number>0</number>
                </property>
               </layout>
              </widget>
              <widget class="QWidget" name="spending_tab">
               <property name="geometry">
                <rect>
                 <x>0</x>
                 <y>0</y>
                 <width>80</width>
                 <height>168</height>
                </rect>
               </property>
               <property name="font">
                <font>
                 <family>Open Sans</family>
                 <pointsize>-1</pointsize>
                 <bold>true</bold>
                </font>
               </property>
               <property name="styleSheet">
                <string notr="true">QWidget {
	vertical-align: top;
	padding: 5px 10px;
	text-shadow: 1px 1px #000;
	
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));

	border: 0px solid #000;
	box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0,.31);
	box-sizing: border-box;
	text-transform: uppercase;
	font-weight: bold;
	color: #f6e5b2;
	font-family: Open Sans;
	font-size: 14px;
	margin: 0px;
}</string>
               </property>
               <attribute name="label">
                <string>Spending</string>
               </attribute>
               <layout class="QVBoxLayout" name="verticalLayout_21">
                <property name="spacing">
                 <number>0</number>
                </property>
                <property name="leftMargin">
                 <number>0</number>
                </property>
                <property name="topMargin">
                 <number>0</number>
                </property>
                <property name="rightMargin">
                 <number>0</number>
                </property>
                <property name="bottomMargin">
                 <number>0</number>
                </property>
               </layout>
              </widget>
              <widget class="QWidget" name="export_tab">
               <property name="geometry">
                <rect>
                 <x>0</x>
                 <y>0</y>
                 <width>80</width>
                 <height>168</height>
                </rect>
               </property>
               <property name="styleSheet">
                <string notr="true">QWidget {
	vertical-align: top;
	padding: 5px 10px;
	text-shadow: 1px 1px #000;
	
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));

	border: 0px solid #000;
	box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0,.31);
	box-sizing: border-box;
	text-transform: uppercase;
	font-weight: bold;
	color: #f6e5b2;
	font-family: Open Sans;
	font-size: 14px;
	margin: 0px;
}</string>
               </property>
               <attribute name="label">
                <string>Export</string>
               </attribute>
               <layout class="QVBoxLayout" name="verticalLayout_25">
                <property name="spacing">
                 <number>0</number>
                </property>
                <property name="leftMargin">
                 <number>0</number>
                </property>
                <property name="topMargin">
                 <number>0</number>
                </property>
                <property name="rightMargin">
                 <number>0</number>
                </property>
                <property name="bottomMargin">
                 <number>0</number>
                </property>
               </layout>
              </widget>
             </widget>
            </item>
            <item>
             <widget class="QWidget" name="status_buttons" native="true">
              <property name="sizePolicy">
               <sizepolicy hsizetype="MinimumExpanding" vsizetype="MinimumExpanding">
                <horstretch>0</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>120</width>
                <height>90</height>
               </size>
              </property>
              <property name="maximumSize">
               <size>
                <width>400</width>
                <height>90</height>
               </size>
              </property>
              <property name="cursor">
               <cursorShape>PointingHandCursor</cursorShape>
              </property>
              <property name="styleSheet">
               <string notr="true">QPushButton {
                border: 1px solid #000;
                  border-top-width: 1px;
                   border-right-width: 1px;
                   border-bottom-width: 1px;
                   border-left-width: 1px;
                   border-top-style: solid;
                 border-right-style: solid;
                  border-bottom-style: solid;
                   border-left-style: solid;
                   border-top-color: rgb(0, 0, 0);
                  border-right-color: rgb(0, 0, 0);
                   border-bottom-color: rgb(0, 0, 0);
                   border-left-color: rgb(0, 0, 0);
                  border-image-source: initial;
                  border-image-slice: initial;
                  border-image-width: initial;
                  border-image-outset: initial;
                border-image-repeat: initial;
                border-radius: 4px;
                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);
                border-image: none;
              color: #FFF;
               text-shadow: 1px 1px #000;
               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);
                font-family: Open Sans;
                font-size: 12px;
               font-weight: bold;
               height: 36px;
                line-height: 36px;
                text-align: center;
				margin: 0px;
           }
            QPushButton::hover {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,
                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);
           }
            QPushButton::pressed {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);
            }
			QPushButton::checked {
				background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,
                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);
				border: 5px inset #FFF;
				box-shadow: none;
			}
            QPushButton::flat {
                border: none;
}</string>
              </property>
              <layout class="QVBoxLayout" name="verticalLayout_30">
               <property name="spacing">
                <number>0</number>
               </property>
               <property name="leftMargin">
                <number>0</number>
               </property>
               <property name="topMargin">
                <number>0</number>
               </property>
               <property name="rightMargin">
                <number>0</number>
               </property>
               <property name="bottomMargin">
                <number>0</number>
               </property>
               <item>
                <widget class="QPushButton" name="clear_item_options">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="cursor">
                  <cursorShape>PointingHandCursor</cursorShape>
                 </property>
                 <property name="toolTip">
                  <string>Clear the selected item and reset the interface</string>
                 </property>
                 <property name="text">
                  <string>Clear Item Options</string>
                 </property>
                 <property name="checkable">
                  <bool>false</bool>
                 </property>
                 <property name="autoDefault">
                  <bool>false</bool>
                 </property>
                 <property name="default">
                  <bool>false</bool>
                 </property>
                 <property name="flat">
                  <bool>false</bool>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QPushButton" name="import_custom_item">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="cursor">
                  <cursorShape>PointingHandCursor</cursorShape>
                 </property>
                 <property name="text">
                  <string>Import Custom Item</string>
                 </property>
                 <property name="checkable">
                  <bool>false</bool>
                 </property>
                 <property name="default">
                  <bool>false</bool>
                 </property>
                 <property name="flat">
                  <bool>false</bool>
                 </property>
                </widget>
               </item>
               <item>
                <widget class="QPushButton" name="simulate_crafting">
                 <property name="sizePolicy">
                  <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                   <horstretch>0</horstretch>
                   <verstretch>0</verstretch>
                  </sizepolicy>
                 </property>
                 <property name="minimumSize">
                  <size>
                   <width>0</width>
                   <height>0</height>
                  </size>
                 </property>
                 <property name="cursor">
                  <cursorShape>PointingHandCursor</cursorShape>
                 </property>
                 <property name="toolTip">
                  <string/>
                 </property>
                 <property name="text">
                  <string>Simulate Crafting</string>
                 </property>
                 <property name="checkable">
                  <bool>false</bool>
                 </property>
                 <property name="checked">
                  <bool>false</bool>
                 </property>
                 <property name="flat">
                  <bool>false</bool>
                 </property>
                </widget>
               </item>
              </layout>
             </widget>
            </item>
           </layout>
          </widget>
         </item>
        </layout>
       </widget>
      </item>
     </layout>
    </widget>
   </item>
  </layout>
 </widget>
 <layoutdefault spacing="0" margin="0"/>
 <customwidgets>
  <customwidget>
   <class>CustomTreeView</class>
   <extends>QTreeView</extends>
   <header location="global">ui.customtreeview</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="modpool_btns"/>
 </buttongroups>
</ui>
