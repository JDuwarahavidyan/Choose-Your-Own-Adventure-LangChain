import { useMemo, useState } from 'react';

function StoryGame({story, onNewStory}) {
    const [selectedNodeId, setSelectedNodeId] = useState(null);

    const activeNodeId = useMemo(() => {
        const rootNodeId = story?.root_node?.id ?? null;

        if (!selectedNodeId) {
            return rootNodeId;
        }

        if (!story?.all_nodes?.[selectedNodeId]) {
            return rootNodeId;
        }

        return selectedNodeId;
    }, [selectedNodeId, story]);

    const currentNode = useMemo(() => {
        if (!activeNodeId || !story?.all_nodes) {
            return null;
        }
        return story.all_nodes[activeNodeId] ?? null;
    }, [activeNodeId, story]);

    const isEnding = Boolean(currentNode?.is_ending);
    const isWinningEnding = Boolean(currentNode?.is_winning_ending);
    const options = isEnding ? [] : (Array.isArray(currentNode?.options) ? currentNode.options : []);


    const chooseOption = (optionId) => {
        setSelectedNodeId(optionId)
    }

    const restartStory = () => {
        setSelectedNodeId(story?.root_node?.id ?? null)
    }

    return <div className="story-game">
        <header className="story-header">
            <h2>{story.title}</h2>
        </header>

        <div className="story-content">
            {currentNode && <div className="story-node">
                <p>{currentNode.content}</p>

                {isEnding ?
                    <div className="story-ending">
                        <h3>{isWinningEnding ? "Congratulations" : "The End"}</h3>
                        {isWinningEnding ? "You reached a winning ending" : "Your adventure has ended."}
                    </div>
                    :
                    <div className="story-options">
                        <h3>What will you do?</h3>
                        <div className="options-list">
                            {options.map((option, index) => {
                                return <button
                                        key={index}
                                        onClick={() => chooseOption(option.node_id)}
                                        className="option-btn"
                                        >
                                        {option.text}
                                    </button>
                            })}
                        </div>
                    </div>
                }
            </div>}

            <div className="story-controls">
                <button onClick={restartStory} className="reset-btn">
                    Restart Story
                </button>
            </div>

            {onNewStory && <button onClick={onNewStory} className="new-story-btn">
                New Story
            </button>}

        </div>
    </div>
}

export default StoryGame